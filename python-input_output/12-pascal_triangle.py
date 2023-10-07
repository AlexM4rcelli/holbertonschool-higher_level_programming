#!/usr/bin/python3
"""Module to a function"""


def pascal_triangle(n):
    """
    Returns a matrix of integers representing the Pascal's triangle of n
    """
    if n <= 0 or not isinstance(n, int):
        return []
    
    triangle = [[1]]
    for i in range(1, n):
        new = [1]
        for j in range(1, i):
            new += [triangle[i - 1][j] + triangle[i - 1][j - 1]]
        new += [1]
        triangle.append(new)
    return triangle
