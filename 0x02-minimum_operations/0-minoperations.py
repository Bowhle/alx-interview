#!/usr/bin/python3
"""
Module to calculate the minimum number of operations
needed to result in exactly n H characters.
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed
    to result in exactly n H characters.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The minimum number of operations needed,
        or 0 if n is impossible to achieve.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
