# !/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


entry_points = {
    'console_scripts': [
        'thriftpy-cli = thriftpy_cli.cmd:client',
    ],
}


setup(
    name="thriftpy-cli",
    version=0.1,
    description="Commandline tools for thrift",
    long_description=open("README.rst").read(),
    author="Haochuan Guo",
    author_email="guohaochuan@gmail.com",
    packages=find_packages(),
    url="https://github.com/wooparadog/thriftpy-cli/",
    entry_points=entry_points,
    install_requires=[
        'click',
        'thriftpy',
        'ipython'
    ],
)
