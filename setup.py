# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='greenhouse_management',
    version=version,
    description='Custom app for managing the data entry, tracking and reporting for commercial greenhouse operations. This apps function is STRICTLY enviromental control.Will track gre',
    author='Brandon Fox, Foxtrot',
    author_email='company@foxtrot.email',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
