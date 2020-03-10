# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2019
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-03-09 13:02'
import os
import io
from setuptools import setup, find_packages


NAME = "pframe"
DESCRIPTION = "PFrame is a basic framework for python"
URL = "https://github.com/Eastwu5788/PFrame"
EMAIL = "wudong@eastwu.cn"
AUTHOR = "LeonardWoo"
REQUIRES_PYTHON = "~=3.2"
VERSION = None

REQUIRED = [
]

package_data = {

}

file_data = [
]

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that!

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here, project_slug, 'version.py')) as f:
        exec(f.read(), about)
else:
    about['version'] = VERSION


setup(
    name=NAME,
    version=about["version"],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=["tests", "tests.*", "examples", "examples.*"]),
    data_files=file_data,
    install_requires=REQUIRED,
    include_package_data=True,
    package_data=package_data,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
