#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for value in row:
            if value != row[-1]:
                print("{:d}".format(value), end= " ")
            else:
                print("{:d}".format(value))
    if not row:
        print()
