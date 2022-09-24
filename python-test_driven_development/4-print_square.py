#!/usr/bin/python3
''' print_square is a module that prints a square given a size as argument'''


def print_square(size):
    ''' conditions for size (only int and >= than 0)'''
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    ''' printing square '''
    for length in range(size):
        for width in range(size):
            print("#", end="")
        print()
