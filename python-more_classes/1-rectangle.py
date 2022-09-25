#!/usr/bin/python3
''' creating a class named Rectangle '''


class Rectangle:
    ''' Instantiation with optional width and height '''
    def __init__(self, width=0, height=0):
        ''' methods (self.width, self.height) treated as variables (through
        the property decorator) that set the object's private attributes '''
        self.width = width
        self.height = height

    ''' getter for width '''
    @property
    def width(self):
        return self.__width

    ''' setter for width '''
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    ''' getter for height '''
    @property
    def height(self):
        return self.__height

    ''' setter for height '''
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
