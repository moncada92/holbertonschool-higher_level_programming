#!/usr/bin/python3

"""
module for read_lines.
"""


def read_lines(filename="", nb_lines=0):
    """number lines text file"""
    num_lines = 0

    with open("my_file_0.txt") as f:
        for line in f:
            num_lines += 1

    if nb_lines <= 0 or nb_lines > num_lines:
        nb_lines = num_lines

    with open("my_file_0.txt") as f2:
        for l in range(nb_lines):
            print(f2.readline(), end="")
