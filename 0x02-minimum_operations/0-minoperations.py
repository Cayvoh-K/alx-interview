#!/usr/bin/python3
"""
method that calculates the least number of operations needed in a character
"""


def minOperations(n):
    """
    A function that calculates the fewest number of operations
    needed to give a result of exactly n H characters in a file
    """

    if n < 1:
        return 0
    elif n == 1:
        return 0
    else:
        operations = 0
        i = 2
        while i <= n:
            while n % i == 0:
                operations += 2
                n //= i
            i += 1
        return operations
