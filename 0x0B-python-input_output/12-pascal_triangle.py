#!/usr/bin/python3
"""module"""


def pascal_triangle(n):
    """Generates Pascal's triangle"""
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]
        for j in range(1, i):
            next_val = triangle[i - 1][j - 1] + triangle[i - 1][j]
            row.append(next_val)
        if i > 0:
            row.append(1)
        triangle.append(row)

    return triangle
