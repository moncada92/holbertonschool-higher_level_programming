#!/usr/bin/python3
"""
Module to class Square
"""

from .rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square the project
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        objt = "[Square] ({}) {}/{}".format(self.id, self.x, self.y)
        return objt+" - {}".format(self.height)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.height = value
        self.width = value

    def update(self, *args, **kwargs):
        i = 0
        for arg in args:
            if i == 0:
                self.id = arg
            elif i == 1:
                self.size = arg
            elif i == 2:
                self.x = arg
            elif i == 3:
                self.y = arg
            i += 1

        if len(args) == 0 or args is None:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
                i += 1

    def to_dictionary(self):
        dic_rect = {}
        dic_rect['x'] = self.x
        dic_rect['y'] = self.y
        dic_rect['id'] = self.id
        dic_rect['size'] = self.width
        return dic_rect
