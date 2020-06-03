#!/usr/bin/python3

"""
this module define class Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This is a class of a Rectangle"""

    def __init__(self, width, height):
        """Initialize"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """return area rectangle"""
        result = self.__height * self.__width
        return result

    def __str__(self):
        """return print operation divider string"""
        return f"[Rectangle] {self.__width}/{self.__height}"
