#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
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
