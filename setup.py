#!/usr/bin/env python3
# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+


from setuptools import setup
from setuptools import find_packages


setup(
    name='wazo_router_confd_client',
    version='0.1',
    description='a simple client library for the wazo router confd HTTP interface',
    author='Wazo Authors',
    author_email='dev@wazo.io',
    url='http://wazo.io',
    packages=find_packages(),
    entry_points={
        'wazo_router_confd_client.commands': [
            'config = wazo_router_confd_client.commands.config:ConfigCommand',
        ],
    }
)
