#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a divisor.

    Args:
        matrix (list): The matrix to be divided.
        div (int or float): The divisor.

    Returns:
        list: A new matrix with elements divided by div, rounded to 2.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If rows of the matrix have different sizes.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.
    """

    error_mess = "matrix must be a matrix (list of lists) of integers/floats"
    if (
        not isinstance(matrix, list) or not
        all(isinstance(row, list) for row in matrix) or not
        all(isinstance(num, (int, float)) for row in matrix for num in row)
    ):
        raise TypeError(error_mess)

    row_sizes = set(len(row) for row in matrix)
    if len(row_sizes) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix
