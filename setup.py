#!/usr/bin/env python
from distutils.core import setup

# Dynamically calculate the version based on mptt2.VERSION
version_tuple = __import__('mptt2').VERSION
version = ".".join([str(v) for v in version_tuple])

setup(
    name = 'django-mptt',
    description = '''Utilities for implementing Modified Preorder Tree Traversal
        with your Django Models and working with trees of Model instances.''',
    version = version,
    author = 'Craig de Stigter',
    author_email = 'craig.ds@gmail.com',
    url = 'http://github.com/django-mptt/django-mptt',
    packages=['mptt2', 'mptt2.templatetags'],
    package_data={'mptt2': ['templates/admin/*', 'locale/*/*/*.*']},
    classifiers = ['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
)
