#!/usr/bin/python3
"""
Function that print a text with 2 new lines after
each of these characters: ., ? and :
"""


def text_indentation(text):
    """Print the square with the caracter #"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        print("{}".format(text[i]), end="")
        if text[i] in [".", "?", ":"]:
            print("")
            print("")
            i += 1
        i += 1
