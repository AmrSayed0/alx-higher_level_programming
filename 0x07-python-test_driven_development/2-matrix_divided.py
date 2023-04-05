#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): A matrix represented as a list of lists of integers or floats.
        div (int or float): The number to divide all elements of the matrix by.

    Returns:
        A new matrix with all elements divided by `div`, rounded to 2 decimal places.
    """
    # Validate input arguments
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Create a new matrix with the divided values
    new_matrix = []
    for row in matrix:
        new_row = []
        for value in row:
            new_row.append(round(value / div, 2))
        new_matrix.append(new_row)

    return new_matrix
