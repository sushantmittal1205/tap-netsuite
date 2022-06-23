#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='tap-netsuite',
    version='1.5.14',
    description='Singer.io tap for extracting data from the NetSuite SOAP',
    author='hotglue',
    url='https://hotglue.xyz/',
    classifiers=['Programming Language :: Python :: 3 :: Only'],
    py_modules=['tap_netsuite'],
    install_requires=[
        'netsuitesdk', # USING THE HOTGLUE VERSION
        'requests',
        'singer-python',
        'xmltodict',
        'jsonpath-ng',
        'jsonschema',
        'pytz'
    ],
    entry_points='''
        [console_scripts]
        tap-netsuite=tap_netsuite:main
    ''',
    packages=find_packages(exclude=['tests']),
    package_data={
        'tap_netsuite.netsuite': ['schemas/*.json']
    },
    include_package_data=True,
)
