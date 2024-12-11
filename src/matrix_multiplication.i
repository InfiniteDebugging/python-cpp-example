%module matrix_multiplication
%{
#include "matrix_multiplication.hpp"
%}

%include <std_vector.i>

%template(VectorInt) std::vector<int>;
%template(VectorVectorInt) std::vector<std::vector<int>>;

std::vector<std::vector<int>> matrix_multiply(const std::vector<std::vector<int>>& A, const std::vector<std::vector<int>>& B);
