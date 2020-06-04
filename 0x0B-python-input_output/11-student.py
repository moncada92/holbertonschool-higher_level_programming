#!/usr/bin/python3
"""
this module define class Student
"""


class Student():
    """This is a class of a Student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """create object with JSON file """
        return self.__dict__
