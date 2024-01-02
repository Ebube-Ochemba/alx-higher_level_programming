#!/usr/bin/python3

"""
2-matrix_divided
Contains a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

    Args:
        matrix (list): A list of integers or floats
        div (int or float): The divisor.

    Return:
        A new matrix representing the division of the 'matrix' by 'div'.

    Raises:
        TypeError: An error occurs when 'matrix' isn't an int/float matrix OR
                   'div' isn't a number OR uneven matrix row size.
        ZeroDivisionError: An error occurs when 'div is = 0.
    """

    error = "matrix must be a matrix (list of lists) of integers/floats"

    if not all(isinstance(i, list) for i in matrix):
        raise TypeError(error)
    if not all(isinstance(j, (int, float)) for i in matrix for j in i):
        raise TypeError(error)

    if not all(len(i) == len(matrix[0]) for i in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(j / div, 2) for j in i] for i in matrix]

    return new_matrix
