#!/usr/bin/python3
'''
    A function that returns True if the object is -exactly- an instance
of the specified class; otherwise False.
'''



def is_same_class(obj, a_class):
    ''' While isinstance caters for inheritance (an instance of a derived
    class is an instance of a base class, too), checking for equality
    of -type- does not (it demands identity of types and rejects instances
    of subtypes, AKA subclasses). '''
    if type(obj) == a_class:
        return True
    else:
        return False
