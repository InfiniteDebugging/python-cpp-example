from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

matrix_multiplication_module = Extension(
    '_matrix_multiplication',
    sources=['src/matrix_multiplication.i', 'src/matrix_multiplication.cpp'],
    include_dirs=['src'],
    swig_opts=['-c++'],
    language='c++',
    extra_compile_args=['-std=c++11'],
)

setup(
    name='matrix_multiplication',
    version='0.1',
    author='b4rdarian',
    description='Matrix multiplication using C++ and SWIG',
    ext_modules=[matrix_multiplication_module],
    py_modules=['matrix_multiplication'],
    package_dir={'': 'src'},
    cmdclass={'build_ext': build_ext},
)