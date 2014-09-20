#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Setup script for py2cytoscape

Yo install, run:

python setup.py install
"""

from setuptools import setup, find_packages

setup(
    name='py2cytoscape',
    version='0.1.0',
    description='Utility package for using Cytoscape and Cytoscape.js from Python',
    author='Keiichiro Ono',
    author_email='kono@ucsd.edu',
    url='http://www.cytoscape.org/',
    license='MIT License',
    keywords=['data visualization'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
    ],
    test_suite='tests',
    packages=find_packages()
)