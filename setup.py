#!/usr/bin/env python
import os
from setuptools import setup, find_packages

__copyright__ = "Copyright (c) 2018 Cisco and/or its affiliates."
__license__ = "MIT"

PACKAGE_NAME = 'bcsoiapis'

PACKAGE_KEYWORDS = [
    'cisco',
    'python',
    'bcs',
    'business critical services',
    'oi api',
]

PACKAGE_CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Intended Audience :: Telecommunications Industry',
    'Intended Audience :: Education',
    'Natural Language :: English',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Topic :: Scientific/Engineering :: Information Analysis',
    'Topic :: System :: Monitoring',
]

INSTALLATION_REQUIREMENTS = [
    'requests',
    'pyjwt',
    'pydantic',
]

project_root = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the project's README.md file
with open(os.path.join(project_root, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=PACKAGE_NAME,
    author='Kristof Van Coillie',
    author_email='kvancoil@cisco.com',
    version='0.1.0',
    url='https://github.com/CiscoDevNet/bcs-apis',
    description='Example implementation to consume the Business Critical Services 3.0 Operations Insights APIs',
    long_description=long_description,
    packages=find_packages('.'),
    include_package_data=True,
    install_requires=INSTALLATION_REQUIREMENTS,
    keywords=' '.join(PACKAGE_KEYWORDS),
    classifiers=PACKAGE_CLASSIFIERS,
    license='MIT; Copyright (c) 2018 Cisco Systems, Inc.'
)
