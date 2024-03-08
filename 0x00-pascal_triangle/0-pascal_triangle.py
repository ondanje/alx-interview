#!/usr/bin/python3
"""
pascal triangle
"""


def pascal_triangle(n):
    """
    function to print out pascal triangle
    """
    if n <= 0:
        return []

    pascaltriangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = pascaltriangle[i - 1][j - 1] + pascaltriangle[i - 1][j]
        pascaltriangle.append(row)

    return pascaltriangle
