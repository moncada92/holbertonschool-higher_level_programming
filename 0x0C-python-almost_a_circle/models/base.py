#!/usr/bin/python3
"""
Module to class Base
"""

import json


class Base:
    """
    Class Base the project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is [None, ""]:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        lists = []
        if list_objs is [None, 0]:
            return lists

        filename = cls.__name__ + ".json"
        for i in list_objs:
            lists.append(i.to_dictionary())

        dicts = cls.to_json_string(lists)

        with open(filename, 'a+', encoding='utf-8') as f:
            return f.write(dicts)
