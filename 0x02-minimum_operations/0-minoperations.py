#!/usr/bin/python3
"""
method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""


def minOperations(n) -> int:
    """
    method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file.
    """
    next_value = 'H'
    body = 'H'
    x = 0

    while (len(body) < n):
        if n % len(body) == 0:
            x += 2
            next_value = body
            body += body
        else:
            x += 1
            body += next_value
    if len(body) != n:
        return 0
    return x
