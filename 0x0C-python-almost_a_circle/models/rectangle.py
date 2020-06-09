#!/usr/bin/python3
"""
Module to class Rectangle
"""

from .base import Base


class Rectangle(Base):
    """
    Class Rectangle the project
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        "Constructor the class"
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        result = self.width * self.height
        return result

    def display(self):
        for n in range(self.y):
            print()
        for i in range(self.height):
            for m in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print('#', end="")
            print()

    def __str__(self):
        objt = "[Rectangle] ({}) {}/{}".format(self.id, self.x, self.y)
        return objt+" - {}/{}".format(self.width, self.height)

    def update(self, *args, **kwargs):

        if args:
            a = ["id", "width", "height", "x", "y"]
            for i, e in enumerate(args):
                setattr(self, a[i], e)
            return
        for x, y in kwargs.items():
            if hasattr(self, x):
                setattr(self, x, y)

    def to_dictionary(self):
        dict_rect = {
            'x': self.x,
            'width': self.width,
            'id': self.id,
            'height': self.height,
            'y': self.y
        }
        return dict_rect
