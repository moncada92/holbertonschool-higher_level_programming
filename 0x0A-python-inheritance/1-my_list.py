#!/usr/bin/python3
"""
this module define class my_list
"""


class MyList(list):
    """This is a class of a MyList"""
    def print_sorted(self):
        """
        Public instance method: that prints the list,
        but sorted (ascending sort)
        """
        print(sorted(self))
