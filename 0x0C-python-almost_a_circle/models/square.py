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
