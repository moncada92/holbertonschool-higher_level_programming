#!/usr/bin/python3
"""
module for MyInt
"""


class MyInt(int):
    """This is a class of a MyInt"""

    def __ne__(self, value):
        return super().__eq__(value)

    def __eq__(self, value):
        return super().__ne__(value)
    