#!/usr/bin/python3
"Module that creates a class with a (private) atribute: size"


class Square:
    ''' Defining a class "Square" and initalizing private
    attribute "__size" with argument passed with instantiation'''
    def __init__(self, size):
        self.__size = size
