#!/usr/bin/python3
''' writing a class Rectangle that inherits from BaseGeometry '''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' with super, I'm calling the method from Rectangle's superclass '''
    def __init__(self, width, height):
        if super().integer_validator("width", width):
            self.__width = width
        if super().integer_validator("height", height):
            self.__height = height
