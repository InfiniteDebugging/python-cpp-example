import os
import sys

import pybind11
from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext


class get_pybind_include(object):
    """Helper class to determine the pybind11 include path
    The purpose of this class is to postpone importing pybind11
    until it is actually installed, so that the `get_include()`
    method can be invoked."""

    def __str__(self):
        return pybind11.get_include()


ext_modules = [
    Extension(
        "matrix_multiplication",
        sources=["bindings/bindings.cpp", "src/matrix_multiplication.cpp"],
        include_dirs=[
            # Path to pybind11 headers
            get_pybind_include(),
            "src",
        ],
        language="c++",
    ),
]

setup(
    name="matrix_multiplication",
    version="0.1",
    author="b4rdarian",
    description="Matrix multiplication using C++ and pybind11",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
)
