#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_l = []
    for i in matrix:
        new_l.append(list(map(lambda x: x ** 2, i)))
    return new_l
