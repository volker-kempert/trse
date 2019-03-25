#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'flask',
    'flask-restful',
    'pyserial',
    'twisted',
]

setup_requirements = []

test_requirements = ['pytest', 'pytest-runner',]

setup(
    author="Volker Kempert",
    author_email='volker.kempert@almedso.de',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Twisted REST api serial exploration",
    entry_points={
        'console_scripts': [
            'trse=trse.cli:main',
            'trsed=trse.trse:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='trse',
    name='trse',
    packages=find_packages(include=['trse']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/volker-kempert/trse',
    version='0.1.0',
    zip_safe=False,
)
