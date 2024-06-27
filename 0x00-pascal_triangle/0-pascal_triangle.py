#!/usr/bin/python3
"""
A list of lists of integers
representing Pascal's triangle of n.
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.
    """
    triangle = []
    if n > 0:
        for row in range(1, n + 1):
            current_row = []
            coefficient = 1
            for col in range(1, row + 1):
                current_row.append(coefficient)
                coefficient = coefficient * (row - col) // col
            triangle.append(current_row)
    return triangle
