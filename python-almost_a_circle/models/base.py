#!/usr/bin/python3
''' This module contains a user-defined class named "Base".
This class will be the “base” of all other classes in this project. '''


import json


class Base:
    ''' private class attribute '''
    __nb_objects = 0
    ''' class constructor '''
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' returns the JSON string representation of list_dictionaries '''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            ''' json.dumps() function convert the raw data into JSON
    format but stores it as a string '''
            return json.dumps(list_dictionaries)
