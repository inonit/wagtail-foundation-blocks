# -*- coding: utf-8 -*-

import re
import os

try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, "__init__.py")).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)

setup(
    name="foundation_blocks",
    version=get_version("foundation_blocks"),
    description="Zurb Foundation Blocks for Wagtail",
    long_description="Implements Foundation components as blocks used by Wagtail",
    author="Rolf Håvard Blindheim",
    author_email="rolf.blindheim@inonit.no",
    url="https://github.com/inonit/wagtail-foundation-blocks",
    download_url="https://github.com/inonit/wagtail-foundation-blocks.git",
    license="MIT License",
    packages=[
        "foundation_blocks",
    ],
    include_package_data=True,
    install_requires=[
        "wagtail"
    ],
    tests_require=[
        "nose",
        "coverage",
    ],
    zip_safe=False,
    test_suite="tests.runtests.start",
    classifiers=[
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
