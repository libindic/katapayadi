#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

name = "katapayadi"

setup(
    name=name,
    version="0.2.0",
    url = "http://silpa.org.in/Katapayadi",
    license="LGPL-3.0",
    description="Decode katapayadi number system",
    author="Santhosh Thottingal",
    author_email="santhosh.thottingal@gmail.com",
    long_description="""
    Katapayadi sankhya is a simplification of Aryabhata's
    Sanskrit numerals, due probably to Haridatta from Kerala.
    In Malayalam it is also known as 'Paralperu'
    For eg: ചണ്ഡാംശുചന്ദ്രാധമകുംഭിപാല represents 31415926536 which
    is π*1000000000000000
    More examples in Malayalam are given in this page
    """,
    packages=find_packages(),
    include_package_data=True,
    setup_requires=['setuptools-git'],
    install_requires=['setuptools','indicsyllabifier','silpa_common'],
    test_suite='tests',
    zip_safe=False,
)
