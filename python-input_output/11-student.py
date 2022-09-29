#!/usr/bin/python3
"""a class that defines a students """


class Student():
    """ Module """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            att_list = {}
            if type(attrs) is list:
                for string in attrs:
                    ''' The hasattr() function returns True if the
                    specified object has the specified attribute,
                    otherwise False '''
                    if hasattr(self, string):
                        ''' Getting the value of the "string" attr.
                        of the instance'''
                        att_list[string] = getattr(self, string)
                return att_list

    def reload_from_json(self, json):
        ''' The update() method inserts the specified items to the dictionary.
        The specified items can be a dictionary, or an iterable object
        with key value pairs. '''
        self.__dict__.update(json)
