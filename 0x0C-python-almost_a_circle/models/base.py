#!/usr/bin/python3
"""
Module to class Base
"""

import json
import os


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
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        lists = []

        if type(list_objs) != list:
            raise TypeError("list_objs must be a list")

        if list_objs is [None, []]:
            return lists

        same_instance = type(list_objs[0])
        for i in list_objs:
            if  type(i) != same_instance:
                raise ValueError("all elements of list_objs must match")
            lists.append(i.to_dictionary())

        dicts = cls.to_json_string(lists)
        filename = cls.__name__ + ".json"

        with open(filename, 'w+', encoding='utf-8') as f:
            f.write(dicts)

    @staticmethod
    def from_json_string(json_string):
        if json_string is [None, ""]:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            tmp = cls(1, 1)
            tmp.update(**dictionary)
            return tmp
        if cls.__name__ == "Square":
            tmp = cls(1)
            tmp.update(**dictionary)
            return tmp

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + '.json'
        list_n = []

        if os.path.exists(filename):
            with open(filename, 'r') as f:
                tmp = cls.from_json_string(f.readline())
                for i in tmp:
                    list_n.append(cls.create(**i))
        return list_n
