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

    def my_print(self):

        if self.__size > 0:
            k = self.__size
            for i in range(0, self.__size):
                j = 0
                while (k > j):
                    print("#", end="")
                    j += 1
                print("")
        else:
            print("")
