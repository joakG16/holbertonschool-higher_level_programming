#!/usr/bin/python3
'''
This is a function that returns the dictionary description with simple
data structure (list, dictionary, string, integer and boolean) for JSON
serialization of an object
'''


def class_to_json(obj):
    ''' just return the object's dictionary, which basically
    contains all the attributes that describe the obj. '''
    return obj.__dict__
