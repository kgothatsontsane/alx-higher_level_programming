#!/usr/bin/python3
"""
12-main
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n
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
