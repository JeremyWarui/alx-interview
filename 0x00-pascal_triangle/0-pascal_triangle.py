#!/usr/bin/python3
""" function that returns Pascal's triangle integers """


def pascal_triangle(n):
    """pascal's triangle function:
    Argument:
    n - number of rows
    Returns a list of integers in each row
    if n <= 0 should return empty list
    """
    if n <= 0:
        return []
    else:
        prev_r = [[1]]
        for i in range(1, n):
            last_r = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    last_r.append(1)
                else:
                    last_r.append(prev_r[-1][j - 1] + prev_r[-1][j])
            prev_r.append(last_r)
        return prev_r
