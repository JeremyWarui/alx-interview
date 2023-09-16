#!/usr/bin/python3
"""island_perimeter(): takes in grdid(int)
    Returns: perimeter of island"""


def island_perimeter(grid):
    """returns perimeter of island"""
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j] == 1):
                perimeter += 4
                # check if right and bottom are 1
                if j + 1 < len(grid[i]) and grid[i][j + 1] == 1:
                    perimeter -= 2
                if (i + 1 < len(grid) and grid[i + 1][j] == 1):
                    perimeter -= 2
    return perimeter
