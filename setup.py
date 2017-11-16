#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from codecs import open
from setuptools import setup, find_packages

VERSION = "0.2.4"

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'License :: OSI Approved :: MIT License',
]

DEPENDENCIES = [
    'msrestazure>=0.4.7'
]

setup(
    name='azure-cli-iot-ext',
    version=VERSION,
    description='Azure IoT CLI Extension',
    long_description='Az CLI extension package focused on IoT commands and functionality.',
    license='MIT',
    author='Microsoft',
    author_email='iotupx@microsoft.com',
    url='https://github.com/azure/azure-iot-cli-extension',
    classifiers=CLASSIFIERS,
    packages=find_packages(),
    package_data={'azext_iot': ['azext_metadata.json']},
    install_requires=DEPENDENCIES
)
