#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    TA = tuple_a + (0, 0)
    TB = tuple_b + (0, 0)
    new = TA[0] + TB[0], TA[1] + TB[1]
    return new
