#!/usr/bin/python3
'''
Write a function that writes an Object to a text file,
using a JSON representation.
'''
import json


def save_to_json_file(my_obj, filename):
    ''' The dump() method is used when the Python objects
    have to be stored in a file. '''
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(my_obj, json_file)
