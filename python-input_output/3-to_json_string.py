#!/usr/bin/python3
'''
This is a function that returns the JSON representation
of an object(string). Known as SERIALIZATION.
Serialization is the process where in we convert the data type of the
raw data, into a JSON format. With that, we mean to say, that the raw
data, usually a dictionary, will now follow
the Javascript Object Notation(JSON) format.
'''

import json


def to_json_string(my_obj):
    '''  json.dumps() function convert the raw data into JSON
    format but stores it as a string'''
    return json.dumps(my_obj)
