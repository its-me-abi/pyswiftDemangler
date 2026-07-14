"""Swift programming language symbol demangler/normalizer library for Python.

Provides a simple interface to demangle Swift symbol names using the official
Swift DLL on Windows.
"""

from .core import demangler

__version__ = "0.1.0"
__author__ = "Abilash"
__all__ = ["demangler"]
