#!/usr/bin/python3
''' say_my_name is a module that prints first name along with
last name through a print statement'''


def say_my_name(first_name, last_name=""):
    ''' this function first checks for name type'''
    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")

    print("My name is " + first_name + " " + last_name)
