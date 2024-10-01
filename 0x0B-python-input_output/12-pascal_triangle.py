#!/usr/bin/python3
"""
This module contains a function to generate Pascal's triangle.

The function `pascal_triangle(n)` returns a list of lists of
integers representing the Pascal`s triangle of a given integer `n`.

Example:
    >>> pascal_triangle(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal`s
    triangle of n
    """
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        row = [1]
        if i > 0:
            row.extend(sum(triangle[-1][j:j+2]) for j in range(i))
        triangle.append(row)
    return triangle
