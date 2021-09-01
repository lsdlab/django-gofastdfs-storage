# django-gofastdfs-storage

集成 [go-fastdfs](https://github.com/sjqzhang/go-fastdfs
) 作为 Django 的静态文件存储后端


已发布至 pypi: https://pypi.org/project/django-gofastdfs-storage/1.0.3/


## pip 安装

```shell
pip install django-gofastdfs-storage==1.0.3
```

## settings.py

```shell
STATICFILES_STORAGE = 'django_gofastdfs_storage.backends.StaticStorage'
DEFAULT_FILE_STORAGE = 'django_gofastdfs_storage.backends.MediaStorage'

GOFASTDFS_ENDPOINT=''
GOFASTDFS_AUTH_TOKEN=''
GOFASTDFS_BUCKET_NAME='djangoadmin'
```
