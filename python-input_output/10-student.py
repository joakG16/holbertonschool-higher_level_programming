#!/usr/bin/python3
''' Writing a class "Student" that defines a student '''


class Student:
    ''' defining instantiation '''
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
