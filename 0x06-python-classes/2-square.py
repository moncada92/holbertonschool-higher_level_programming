#!/usr/bin/python3
"""this module  defines the Square class"""


class Square:
    """This is a class of a square"""
    def __init__(self, size=0):
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
