#!/usr/bin/python3

"""
module for read_file.
"""


def read_file(filename=""):
    """Read a text file"""
    with open("my_file_0.txt", 'r',encoding="utf-8") as f:
        for line in f:
            print(line, end="")
