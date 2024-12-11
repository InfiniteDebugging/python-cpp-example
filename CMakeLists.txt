cmake_minimum_required(VERSION 3.4...3.18)
project(matrix_multiplication)

find_package(pybind11 REQUIRED)

include_directories(src)
pybind11_add_module(matrix_multiplication bindings/bindings.cpp src/matrix_multiplication.cpp)
