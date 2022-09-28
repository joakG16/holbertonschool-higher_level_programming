#!/usr/bin/python3
''' Write a function that returns an object (Python data structure)
represented by a JSON string, known as DESERIALIZATION.
Deserialization is the process of decoding the data that
is in JSON format into native data type.
'''
import json


def from_json_string(my_str):
    ''' loads() : to deserialize a JSON document to a Python object. '''
    return json.loads(my_str)
