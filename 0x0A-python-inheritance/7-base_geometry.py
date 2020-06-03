#!/usr/bin/python3
"""
this module define class base_geometry
"""


class BaseGeometry():
    """This is a class of a base_geometry"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(self.name))

        if value == 0:
            raise ValueError("{} must be greater than 0".format(self.name))

        if value < 0:
            raise ValueError("{} must be greater than 0".format(self.name))

        self.value = value
