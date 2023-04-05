#!/usr/bin/python3

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices using NumPy.

    Args:
        m_a: the first matrix as a list of lists of integers/floats.
        m_b: the second matrix as a list of lists of integers/floats.

    Returns:
        The product of the 2 matrices as a NumPy array.

    Raises:
        ValueError: if the matrices cannot be multiplied.
    """
    # Convert the matrices to NumPy arrays
    a = np.array(m_a)
    b = np.array(m_b)

    # Check if the matrices can be multiplied
    if a.shape[1] != b.shape[0]:
        raise ValueError("Matrices cannot be multiplied")

    # Multiply the matrices using NumPy
    c = np.dot(a, b)

    # Convert the result back to a list of lists
    return c.tolist()
