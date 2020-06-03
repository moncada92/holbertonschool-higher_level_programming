#!/usr/bin/python3
"""
this module define function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """This is a function of a is_kind_of_class"""
    if type(obj) is a_class or isinstance(obj, a_class):
        return True
    else:
        return False
