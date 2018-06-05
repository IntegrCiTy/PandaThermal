#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import pandathermal

setup(

    name='pandangas',

    version=pandathermal.__version__,

    packages=find_packages(),

    author="Pablo Puerto",

    author_email="pablo.puerto@mines-albi.fr",

    description="District heating and cooling network design and simulation tool, largely inspired by PandaPower",

    long_description=open('README.md').read(),

    install_requires=["pandas", "networkx >= 2"],

    include_package_data=True,

    url='',

    classifiers=[
        "Natural Language :: English",
        "Operating GraphCreator :: OS Independent",
        "Programming Language :: Python :: 3.5",
        "Topic :: Simulation",
    ]

)
