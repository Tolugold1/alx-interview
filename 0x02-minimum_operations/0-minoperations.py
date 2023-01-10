#!/usr/bin/python3
"""In a text file, there is a single character H.
 Your text editor can execute only two operations
 in this file: Copy All and Paste. Given a number
n, write a method that calculates the fewest number
of operations needed to result in exactly n H
characters in the file."""


def minOperations(n: int) -> int:
    """calculates the fewest number of operations
    needed to result in exactly n H characters
    in the file"""
    process = 2
    op = 0
    if (n == None or n < 0):
        return 0
    elif (n == 1):
        return 1
    elif (n > 1):
        while (n > 1):
            while n % 2 == 0:
                op += process
                n /= process
            process += 1
        return op
