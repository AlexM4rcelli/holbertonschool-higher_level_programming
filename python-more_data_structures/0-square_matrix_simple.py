#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = lambda x: x**2
    new = list(map(lambda row: list(map(square, row)), matrix))
    return new
