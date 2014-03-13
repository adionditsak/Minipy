#!/usr/bin/env python

import mini

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name=mini.__title__,
    version=mini.__version__,
    description=mini.__description__,
    author=mini.__author__,

    url="http://aarvik.dk",
    packages=['mini'],
    package_dir={'mini': 'mini'},
)
