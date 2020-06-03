#!/usr/bin/python3
"""
this module define function inherits_from
"""


def inherits_from(obj, a_class):
    """This is a function of a inherits_from"""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
