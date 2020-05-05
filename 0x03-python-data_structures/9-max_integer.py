#!/usr/bin/python3
def max_integer(my_list=[]):
    maxint = None

    for i in my_list:
        if maxint is None:
            maxint = i
        if i > maxint:
            maxint = i
    return maxint
