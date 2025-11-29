#!/usr/bin/python3
'''This is intended to create pascal triangle'''


def pascal_triangle(n):
    """Returns a list of lists representing Pascal's triangle of n."""
    if n <= 0:
        return []

    triangle = []
    row = [1]
    triangle.append(row)

    for _ in range(1, n):
        prev = row
        row = [1]

        for i in range(len(prev) - 1):
            row.append(prev[i] + prev[i + 1])

        row.append(1)

        triangle.append(row)

    return triangle
