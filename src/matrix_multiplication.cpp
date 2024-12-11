# include "matrix_multiplication.hpp"


std::vector<std::vector<int>> matrix_multiply(const std::vector<std::vector<int>>& A, const std::vector<std::vector<int>>& B) {
        int n = A.size();
        int m = B[0].size();
        int k = A[0].size();
        std::vector<std::vector<int>> C(n, std::vector<int>(m, 0));

        for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                        for (int l = 0; l < k; l++) {
                                C[i][j] += A[i][l] * B[l][j];
                        }
                }
        }
        return C;
}
