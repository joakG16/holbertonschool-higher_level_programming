#!/usr/bin/python3
''' writing a class Rectangle that inherits from Rectangle (9-rectangle.py) '''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' instantiation method '''
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__height = size
        self.__width = size

    ''' defining an area method '''
    def area(self):
        return self.__height * self.__width

    ''' defining a string reperesentation method '''
    def __str__(self):
        ''' styling the string representation of the object '''
        return f'[Rectangle] {self.__width}/{self.__height}'
        # f-Strings format 