#!/usr/bin/python3

from matrix_divided import matrix_divided

# Test case 1: divide each element of a 2x3 matrix by 2
matrix1 = [
    [1, 2, 3],
    [4, 5, 6]
]
div1 = 2
print(matrix_divided(matrix1, div1))

# Test case 2: divide each element of a 3x3 matrix by 3
matrix2 = [
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15]
]
div2 = 3
print(matrix_divided(matrix2, div2))

# Test case 3: divide each element of a 4x4 matrix by 4
matrix3 = [
    [16, 17, 18, 19],
    [20, 21, 22, 23],
    [24, 25, 26, 27],
    [28, 29, 30, 31]
]
div3 = 4
print(matrix_divided(matrix3, div3))
