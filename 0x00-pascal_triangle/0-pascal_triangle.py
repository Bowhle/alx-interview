#!/usr/bin/python3
"""
This function returns Pascal's Triangle up to n rows
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    Pascal's triangle of n
    Args:
        n (int): Number of rows to generate
    Returns:
        list: Empty list if n <= 0, otherwise a list of
        lists representing Pascal's triangle
    """
    if n <= 0:
        return []
    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        current_row = [1]

        for j in range(1, i):
            current_row.append(prev_row[j-1] + prev_row[j])

        current_row.append(1)

        # Appends the current row to the triangle
        triangle.append(current_row)

    return triangle
