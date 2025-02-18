#!/usr/bin/env python

from os.path import exists
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name='django-adminlte4',
    version='0.1.0',
    author='hehenischal',
    author_email='nischallc56@gmail.com',
    packages=find_packages(),
    scripts=[],
    url='https://github.com/hehenischal/django-adminlte4',
    license='MIT',
    description='Admin LTE templates, admin theme, and template tags for Django',
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    # Any requirements here, e.g. "Django >= 1.1.1"
    install_requires=[
        'django>=4.0',
    ],
    python_requires='>=3.6',
)
