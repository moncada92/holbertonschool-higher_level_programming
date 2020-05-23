#!/usr/bin/python3
"""
Function print my first and last name
Return: first and last name

"""


def say_my_name(first_name, last_name=""):
    """print my first and last name"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
