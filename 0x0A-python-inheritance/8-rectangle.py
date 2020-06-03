#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
this module define class Rectangle
"""


class Rectangle(BaseGeometry):
    """This is a class of a Rectangle"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)
