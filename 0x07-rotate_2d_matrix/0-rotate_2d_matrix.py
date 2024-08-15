#!/usr/bin/python3
""" Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """  Rotate 2D Matrix
    """
    for x, y in enumerate(zip(*reversed(matrix))):
        matrix[x] = list(y)


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    """ Rotate 2D Matrix """
    rotate_2d_matrix(matrix)
    print(matrix)
