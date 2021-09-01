from setuptools import setup

with open('README.md', 'r') as f:
    readme = f.read()

setup(
    name='django-gofastdfs-storage',
    version="1.0.2",
    author="JC",
    author_email="lsdvincent@gmail.com",
    maintainer="JC",
    maintainer_email="lsdvincent@gmail.com",
    license='MIT',
    description='Django storage backends for go-fastdfs',
    long_description=readme,
    long_description_content_type='text/markdown',
    packages=['django_gofastdfs_storage'],
    install_requires=['django>=2.1.10',
                      'requests>=2.26.0'],
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
        'Programming Language :: Python :: 3.9',
        'Framework :: Django',
    ],
)
