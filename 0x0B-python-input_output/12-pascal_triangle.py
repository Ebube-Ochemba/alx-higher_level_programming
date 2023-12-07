#!/usr/bin/python3

"""
12-pascal_triangle
"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing
    the Pascal’s triangle of n.

    Parameters
    ----------
    n : int
        The size of the triangle.

    return: An empty list if n <= 0, else a list.
    """

    if n <= 0:
        return []

    triangle = [[1]]
    for row in range(1, n):
        new_row = [1]
        for idx in range(1, row):
            new_row.append(triangle[row-1][idx-1] + triangle[row-1][idx])
        new_row.append(1)
        triangle.append(new_row)
    return triangle
