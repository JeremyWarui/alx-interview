#!/usr/bin/python3

"""rotate_2d_matrix(matrix): rotate 2D matrix"""


def rotate_2d_matrix(matrix):
    """rotates a 2d matrix"""
    matrix[:] = list(zip(*matrix))
    # reverse each row
    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]
    matrix[:] = [list(row) for row in matrix]
