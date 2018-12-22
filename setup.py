#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='israel-rail-api',
    version='0.0.1',
    packages=['israelrailapi'],
    url='https://github.com/sh0oki/israel-rails-api',
    install_requires=['requests',
                      'jsoncomment',
                      'pytz'],
    license='MIT',
    author='sh0oki',
    description='Israeli Rail unofficial API'
)
