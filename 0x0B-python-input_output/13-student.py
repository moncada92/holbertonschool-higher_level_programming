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

    def to_json(self, attrs=None):
        """create object with JSON file """
        if type(attrs) is not list:
            return self.__dict__
        dict = {}

        for i in attrs:
            is_attrs = getattr(self, i, None)
            if is_attrs is not None:
                dict[i] = is_attrs
        return dict

    def reload_from_json(self, json):
        """change all attributes"""
        for p, r in json.items():
            self.__dict__[p] = r
