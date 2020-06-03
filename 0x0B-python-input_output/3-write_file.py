#!/usr/bin/python3

"""
module for write_file.
"""


def write_file(filename="", text=""):
    """write in the file"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
