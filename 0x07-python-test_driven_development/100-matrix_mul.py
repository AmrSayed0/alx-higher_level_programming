#!/usr/bin/python3

def matrix_mul(m_a, m_b):
    # Check if m_a and m_b are lists
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")

    # Check if m_a and m_b are lists of lists
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")

    # Check if m_a and m_b are not empty
    if len(m_a) == 0 or len(m_a[0]) == 0 or len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_a can't be empty or m_b can't be empty")

    # Check if m_a and m_b contain only integers or floats
    for row in m_a:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    # Check if m_a and m_b are rectangles (all 'rows' should be of the same size)
    if not all(len(row) == len(m_a[0]) for row in m_a) or not all(len(row) == len(m_b[0]) for row in m_b):
        raise ValueError("each row of m_a must be of the same size or each row of m_b must be of the same size")

    # Check if m_a and m_b can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Multiply matrices
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            element = 0
            for k in range(len(m_a[0])):
                element += m_a[i][k] * m_b[k][j]
            row.append(element)
        result.append(row)
    return result
