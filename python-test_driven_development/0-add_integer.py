#!/usr/bin/python3
''' A function that adds two integers'''


def add_integer(a, b=98):
    ''' check if the values passed are correct type/acceptable value
    b value is set to 98 by default, so it works with one argument'''
    if isinstance(a, (int, float)) is False or a is None:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)) is False:
        raise TypeError("b must be an integer")
    ''' casted to int before doing the sum '''
    return int(a) + int(b)
