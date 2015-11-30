#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from docker_travis_php import __version__

try:
    from setuptools import setup
    setup  # workaround for pyflakes issue #13
except ImportError:
    from distutils.core import setup

# Hack to prevent stupid TypeError: 'NoneType' object is not callable error on
# exit of python setup.py test # in multiprocessing/util.py _exit_function when
# running python setup.py test (see
# http://www.eby-sarna.com/pipermail/peak/2010-May/003357.html)
try:
    import multiprocessing
    multiprocessing
except ImportError:
    pass


def open_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname))


setup(
    name='docker-travis-php',
    version=__version__,
    author='Jose Diaz-Gonzalez',
    author_email='docker-travis-php@josediazgonzalez.com',
    packages=['docker_travis_php'],
    scripts=['bin/docker-travis-php'],
    url='http://github.com/josegonzalez/docker-travis-php',
    license=open('LICENSE.txt').read(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    description='Shits out a simple dockerfile for php projects based upon a .travis.yml',
    long_description=open_file('README.rst').read(),
    install_requires=open_file('requirements.txt').readlines(),
    zip_safe=True,
)
