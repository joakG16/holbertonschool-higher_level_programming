#!/usr/bin/python3
'''
Write a function that creates an Object from a “JSON file”
(de-serialization)
'''
import json


def load_from_json_file(filename):
    ''' json.load() takes a file object and returns the json object. '''
    with open(filename, mode='r', encoding='utf-8') as from_json_file:
        json_data_to_obj = json.load(from_json_file)
        return json_data_to_obj
