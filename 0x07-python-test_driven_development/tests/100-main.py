#!/usr/bin/python3

from matrix_multiplication import matrix_mul

# Test case 1
m_a = [[1, 2], [3, 4]]
m_b = [[1, 2], [3, 4]]
result = matrix_mul(m_a, m_b)
print(result)

# Test case 2
m_a = [[1, 2]]
m_b = [[3, 4], [5, 6]]
result = matrix_mul(m_a, m_b)
print(result)
