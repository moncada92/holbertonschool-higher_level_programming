#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None or matrix == [[]]:
        print()
    for row in matrix:
        k = 1
        for element in row:
            if k < len(row):
                print("{:d} ".format(element), end='')
            else:
                print("{:d}".format(element))

            k += 1
