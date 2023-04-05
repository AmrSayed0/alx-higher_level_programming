#!/usr/bin/python3

from typing import List

import numpy as np


def lazy_matrix_mul(m_a: List[List[int]], m_b: List[List[int]]) -> List[List[int]]:
    """
    Multiplies 2 matrices using NumPy.

    Args:
        m_a: the first matrix as a list of lists of integers.
        m_b: the second matrix as a list of lists of integers.

    Returns:
        The product of the 2 matrices as a list of lists of integers.

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


if __name__ == "__main__":
    # Test the function with some examples
    a = [[1, 2], [3, 4]]
    b = [[1, 2], [3, 4]]
    c = lazy_matrix_mul(a, b)
    print(c)  # Output: [[7, 10], [15, 22]]

    a = [[1, 2]]
    b = [[3, 4], [5, 6]]
    c = lazy_matrix_mul(a, b)
    print(c)  # Output: [[13, 16]]
