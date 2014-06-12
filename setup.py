#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import iconfonts

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = iconfonts.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='IconFonts',
    version=version,
    description="""This package provides a toolkit to render icon-font glyphs.""",
    long_description=readme + '\n\n' + history,
    author='joke2k',
    author_email='joke2k@gmail.com',
    url='https://github.com/joke2k/iconfonts',
    packages=[
        'iconfonts',
        'iconfonts.django',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="MIT",
    zip_safe=False,
    keywords='iconfonts',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)