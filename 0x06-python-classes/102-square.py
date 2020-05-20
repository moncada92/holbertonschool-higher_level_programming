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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int:
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        result_area = self.__size * self.__size
        return result_area

    def __gt__(self, other):
        """greater"""
        return self.area() > other.area()

    def __lt__(self, other):
        """less"""
        return self.area() < other.area()

    def __eq__(self, other):
        """equal"""
        return self.area() == other.area()

    def __ge__(self, other):
        """greater than or equal"""
        return self.area() >= other.area()

    def __le__(self, other):
        """less than or equal"""
        return self.area() <= other.area()

    def __ne__(self, other):
        """not equal operator"""
        return self.area() != other.area()
