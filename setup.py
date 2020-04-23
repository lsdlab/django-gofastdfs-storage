from setuptools import setup, find_packages


with open('README.md', 'rb') as f:
    readme = f.read().decode('utf-8')

setup(
    name='django-gofastdfs-storage',
    version="1.0.0",
    author="JC",
    author_email="lsdvincent@gmail.com",
    maintainer="JC",
    maintainer_email="lsdvincent@gmail.com",
    license='MIT',
    description='Django storage backends for go-fastdfs',
    long_description=readme,
    packages=['django_gofastdfs_storage'],
    install_requires=['django>=2.2.10',
                      'requests>=2.23.0'],
    include_package_data=True,
    url='https://github.com/lsdlab/django-gofastdfs-storage',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Framework :: Django',
    ],
)
