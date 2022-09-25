#!/usr/bin/python3
''' creating a class named Rectangle, which calculates area and perimeter '''


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

    ''' calculates and returns the area of a rectangle '''
    def area(self):
        return self.width * self.height

    ''' calculates and returns the area of a rectangle '''
    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height * 2) + (self.width * 2)

    def __str__(self):
        if self.height == 0 or self.width == 0:
            return ""
        str_rep = ""
        for lines in range(self.__height - 1):
            str_rep += ("#" * self.__width + "\n")
        str_rep += ("#" * self.__width)  # last line of "#'s"
        # without extra newline
        return str_rep
