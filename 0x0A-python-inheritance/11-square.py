#!/usr/bin/python3

"""
this module define class Square
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This is a class of a Square"""

    def __init__(self, size):
        """Initialize"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """return area the Square"""
        return self.__size * self.__size

    def __str__(self):
        """return print operation divider string"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
