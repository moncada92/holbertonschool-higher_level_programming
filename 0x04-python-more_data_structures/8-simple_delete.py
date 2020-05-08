#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    iskey = False
    for llave in a_dictionary:
        if llave == key:
            iskey = True

    if iskey:
        del a_dictionary[key]

    return a_dictionary
