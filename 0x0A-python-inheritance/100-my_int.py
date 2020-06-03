#!/usr/bin/python3

"""
module for MyInt
"""


class MyInt(int):
    """This is a class of a MyInt"""

    def __ne__(self, other):
        return super().__eq__(other)

    def __eq__(self, other):
        return super().__ne__(other)
