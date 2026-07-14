#!/usr/bin/env python
"""Setup script for pyswiftdemangler package."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pyswiftdemangler",
    version="0.1.0",
    author="Abilash",
    author_email="its-me-abi@github.com",
    description="A Swift programming language symbol demangler/normalizer library for Python on Windows",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/its-me-abi/pyswiftDemangler",
    packages=find_packages(),
    package_data={
        'pyswiftdemangler': ['lib/*.dll'],
    },
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'pyswiftdemangler=pyswiftdemangler.cli:main',
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development :: Libraries",
    ],
    keywords="swift demangler symbol-demangling swift-language",
)
