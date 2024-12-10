import unittest
import faulthandler
import matrix_multiplication

faulthandler.enable()  # Enable faulthandler for better debugging

class TestMatrixMultiplication(unittest.TestCase):
    
    def test_multiply(self):
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]
        expected_result = [[19, 22], [43, 50]]
        result = matrix_multiplication.matrix_multiply(A, B)
        self.assertEqual(result, expected_result)

    # def test_empty_matrices(self):
    #     A = []
    #     B = []
    #     expected_result = []
    #     result = matrix_multiplication.matrix_multiply(A, B)
    #     self.assertEqual(result, expected_result)

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()