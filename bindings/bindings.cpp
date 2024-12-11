#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "matrix_multiplication.hpp"

namespace py = pybind11;

PYBIND11_MODULE(matrix_multiplication, m) {
    m.def("matrix_multiply", &matrix_multiply, "Matrix multiplication function");
}
