#!/usr/bin/python3
''' writing a class Rectangle that inherits from Rectangle (9-rectangle.py) '''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' instantiation method '''
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    ''' defining an area function'''
    def area(self):
        return self.__size ** 2

    ''' string representation method '''
    def __str__(self):
        ''' styling the string representation of the object '''
        return f'[Square] {self.__size}/{self.__size}'
        # f-Strings format
