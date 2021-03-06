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
        if type(list_objs) != list and list_objs is not None:
            raise TypeError("list_objs must be a list")
        if list_objs is None or list_objs == []:
            out = []
        else:
            first = type(list_objs[0])
            if any(type(i) != first for i in list_objs):
                raise ValueError("all elements of list_objs must match")
            out = [i.to_dictionary() for i in list_objs]
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(cls.to_json_string(out))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "":
            return []
        if type(json_string) != str:
            raise TypeError("json_string must be a string")

        json_dates = json.loads(json_string)

        for date in json_dates:
            if type(date) != dict:
                raise ValueError("json_string must contain dictionaries")

        return json_dates

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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        if type(list_objs) != list and list_objs is not None:
            raise TypeError("list_objs must be a list")
        if list_objs is None or list_objs == []:
            out = []
        else:
            first = type(list_objs[0])
            if any(type(i) != first for i in list_objs):
                raise ValueError("all elements of list_objs must match")
            out = [i.to_dictionary() for i in list_objs]
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as f:
            f.write(cls.to_json_string(out))

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + '.csv'
        list_n = []

        if os.path.exists(filename):
            with open(filename, 'r') as f:
                tmp = cls.from_json_string(f.readline())
                for i in tmp:
                    list_n.append(cls.create(**i))
        return list_n
