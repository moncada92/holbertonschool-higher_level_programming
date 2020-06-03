#!/usr/bin/python3

"""
module for append_write_file.
"""


def append_write(filename="", text=""):
    """write append in the file"""
    with open(filename, 'a+', encoding="utf-8") as f:
        return f.write(text)
