#!/usr/bin/python3
"""
Function divider a itmes the matrix
Return: matrix / for 3

"""


def matrix_divided(matrix, div):

    """Function that divide a matrix"""
    divide = []
    errsize = "Each row of the matrix matrix must have the same size"
    errtype = "matrix must be a matrix (list of list) of integers/floats"
    rowback = len(matrix[0])

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(len(matrix)):
        divide.append([])
        if(len(matrix[i]) is not rowback):
            raise TypeError(errsize)
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) not in [int, float]:
                raise TypeError(errtype)
            divide[i].append(round(matrix[i][j] / div, 2))
            rowback = len(matrix[i])
    return divide
