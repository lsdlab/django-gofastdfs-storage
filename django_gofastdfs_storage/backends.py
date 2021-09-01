import os
import base64
import six
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings
from django.core.files.storage import Storage
from django.utils.deconstruct import deconstructible
import requests


def _get_config(name, default=None):
    config = os.environ.get(name, getattr(settings, name, default))
    if config is not None:
        if isinstance(config, six.string_types):
            return config.strip()
        else:
            return config
    else:
        raise ImproperlyConfigured(
            "'%s not found in env variables or setting.py" % name)


@deconstructible
class GoFastDFSStorage(Storage):
    def __init__(self, end_point=None, auth_token=None, bucket_name=None):
        self.end_point = end_point if end_point else _get_config(
            'GOFASTDFS_ENDPOINT')
        self.auth_token = auth_token if auth_token else _get_config(
            'GOFASTDFS_AUTH_TOKEN')
        self.bucket_name = bucket_name if bucket_name else _get_config(
            'GOFASTDFS_BUCKET_NAME')

    def _open(self, name, mode='rb'):
        pass

    def save_gofastdfs_static(self, file_path):
        url = self.end_point
        files = {'file': open(file_path, 'rb')}
        options = {'auth_token': self.auth_token,
                   'output': 'json', 'path': self.bucket_name, 'scene': ''}
        try:
            res = requests.post(url, data=options, files=files)
            return res
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            raise SystemExit(e)

    def _save(self, name, content):
        response = self.save_gofastdfs_static(content.__str__())
        if response.status_code != 200:
            raise Exception("gofastdfs upload file failed")
        url = response.json()['path']
        return url

    def url(self, name):
        return self.end_point.replace('upload', '') + self.bucket_name + "/" + name.split('/')[-1] + '?download=0'

    def exists(self, name):
        return False


class MediaStorage(GoFastDFSStorage):
    def __init__(self):
        super(MediaStorage, self).__init__()


class StaticStorage(GoFastDFSStorage):
    def __init__(self):
        super(StaticStorage, self).__init__()
