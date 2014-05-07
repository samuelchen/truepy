#!/usr/bin/env python
# coding: utf8

import os
import sys


# The directories in which the packages can be found
PACKAGE_DIR = {
    'truepy': 'lib/truepy'}


def setup(**kwargs):
    global INFO, README, CHANGES, PACKAGE_DATA, PACKAGE_DIR
    setuptools.setup(
        name = 'truepy',
        version = '.'.join(str(i) for i in INFO['version']),
        description = ''
            'A Python library to create TrueLicense license files.',
        long_description = README + '\n\n' + CHANGES,

        install_requires = [],
        setup_requires = [],

        author = INFO['author'],
        author_email = 'moses.palmer@gmail.com',

        url = 'https://github.com/moses-palmer/truepy',

        packages = setuptools.find_packages(
            os.path.join(
                os.path.dirname(__file__),
                'lib'),
            exclude = ['tests', 'tests.suites']),
        package_dir = PACKAGE_DIR,
        zip_safe = True,

        license = 'GPLv3',
        platforms = ['linux', 'windows'],
        classifiers = [],

        **kwargs)


import setuptools


# Read globals from truepy._info without loading it
INFO = {}
with open(os.path.join(
        os.path.dirname(__file__),
        'lib',
        'truepy',
        '_info.py')) as f:
    for line in f:
        try:
            name, value = (i.strip() for i in line.split('='))
            if name.startswith('__') and name.endswith('__'):
                INFO[name[2:-2]] = eval(value)
        except ValueError:
            pass


try:
    # Read README
    with open(os.path.join(
            os.path.dirname(__file__),
            'README.rst')) as f:
        README = f.read()


    # Read CHANGES
    with open(os.path.join(
            os.path.dirname(__file__),
            'CHANGES.rst')) as f:
        CHANGES = f.read()
except IOError:
    README = ''
    CHANGES = ''


# Arguments passed to setup
setup_arguments = {}


try:
    setup(**setup_arguments)
except Exception as e:
    try:
        sys.stderr.write(e.args[0] % e.args[1:] + '\n')
    except:
        sys.stderr.write(str(e) + '\n')
