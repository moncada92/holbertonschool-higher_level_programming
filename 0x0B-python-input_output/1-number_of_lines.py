#!/usr/bin/python3

"""
module for number_lines.
"""


def number_of_lines(filename=""):
    """number lines text file"""
    num_lines = 0
    with open(filename, encoding="utf-8") as f:
        for line in f:
            num_lines += 1

    return num_lines
