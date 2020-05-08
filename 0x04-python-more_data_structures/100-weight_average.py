#!/usr/bin/python3
def weight_average(my_list=[]):
    num = 0
    den = 0
    result = 0.0
    if len(my_list) != 0:
        for i, j in my_list:
            num = num + (i * j)
            den = den + j

    result = num / den
    return result
