#!/usr/bin/python3
''' 
    A function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class; otherwise False
'''


def is_kind_of_class(obj, a_class):
    ''' isistance is used here because it handles properly
    inheritance, subclasses basically '''
    if isinstance(obj, a_class) is True:
        return True
    else:
        return False
