#!/usr/bin/env python

import minipy

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name=minipy.__title__,
    version=minipy.__version__,
    description=minipy.__description__,
    author=minipy.__author__,
    url="http://aarvik.dk",
    packages=['minipy'],
    )
