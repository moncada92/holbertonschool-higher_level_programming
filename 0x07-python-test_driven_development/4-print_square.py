#!/usr/bin/python3
"""
Function print square
Return: squares

"""


def print_square(size):
    """print square"""
    if type(size) is not int:
        raise("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(0, size):
        j = 0
        while (size > j):
            print("#", end="")
            j += 1
        print("")
