#!/usr/bin/python3
"""this module  defines the Square class"""


class Square:
    """This is a class of a square"""
    def __init__(self, size=0, position=(0, 0)):
        if (type(size) is int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

        self.__err = "position must be a tuple of 2 positive integers"

        if type(position) != tuple or len(position) != 2:
            raise TypeError(self.__err)

        if (type(position[0]) is not int) or (type(position[1]) is not int):
            raise TypeError(self.__err)

        if position[0] < 0 and position[1] < 0:
            raise ValueError(self.__err)

        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int:
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, values):
        if type(values) != tuple or len(values) != 2:
            raise TypeError(self.__err)

        if (type(values[0]) is not int) or (type(values[1]) is not int):
            raise TypeError(self.__err)

        if (values[0] < 0) or (values[1] < 0):
            raise TypeError(self.__err)

        self.__position = values

    def area(self):
        result_area = self.__size * self.__size
        return result_area

    def my_print(self):

        if self.__size > 0:
            k = self.__size

            for r in range(0, self.__position[1]):
                print()

            for i in range(0, self.__size):
                j = 0

                for n in range(0, self.__position[0]):
                    print(" ", end="")
                while (k > j):
                    print("#", end="")
                    j += 1
                print("")
        else:
            print("")
