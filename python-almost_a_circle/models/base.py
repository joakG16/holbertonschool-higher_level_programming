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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): list of instances that inherits from Base
            (can be rectangle, square)
        """
        with open(cls.__name__ + ".json", mode="w", encoding="utf-8") as file:
            if list_objs is None:
                file.write(cls.to_json_string(None))
            else:
                obj_dicts = [obje.to_dictionary() for obje in list_objs]
                file.write(cls.to_json_string(obj_dicts))
