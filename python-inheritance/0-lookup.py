#!/usr/bin/python3
''' a function that returns the list of available
attributes and methods of an object '''


def lookup(obj):
    ''' dir() tries to return a valid list of attributes
    of the object it is called upon. '''
    return dir(obj)
