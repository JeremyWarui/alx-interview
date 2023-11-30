#!/usr/bin/python3
"""island_perimeter(grid)
Args: Function that takes in a list of integers
Returns: the perimeter of the island described as grid

Grid is a list of integers where:
    0 represents water
    1 represents land
Each cell is a square with a side length of 1
"""


def island_perimeter(grid):
    """island perimeter func
    Input: list of integers
    Returns: perimeter"""

    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                if j == len(grid) - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
