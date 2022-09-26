#!/usr/bin/python3
''' creating a class named Rectangle'''


class Rectangle:
    ''' creating a counter for created/deleted instances '''
    number_of_instances = 0  # class attribute
    print_symbol = "#"  # class attribute

    ''' Instantiation with optional width and height '''
    def __init__(self, width=0, height=0):
        ''' methods (self.width, self.height) treated as variables (through
        the property decorator) that set the object's private attributes '''
        self.width = width
        self.height = height
        type(self).number_of_instances += 1  # add when a new obj. is created

    ''' method called to delete instance'''
    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1  # decrement if an obj. is deleted

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

    ''' computes a string containing the value, or more consicesly
    the pattern (with symbol using public class attribute
    print_symbol) of the rectangle '''
    def __str__(self):
        if self.height == 0 or self.width == 0:
            return ""
        str_val = ""
        for lines in range(self.__height - 1):
            str_val += str(self.print_symbol) * self.__width + "\n"
        str_val += str(self.print_symbol) * self.__width  # last line of symb.
        # without extra newline
        return str_val

    ''' With the return value of repr() it should be possible to recreate
    our object using eval() -> This function takes a string and evaluates it's
    content as Python code. repr() makes coder-string-friendly
    (code basically)'''
    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'
        # f-Strings format

    ''' With staticmethods, neither self (the object instance) nor cls
    (the class) is implicitly passed as the first argument. They behave
    like plain functions except that you can call them from an instance
    or the class. Staticmethods are used to group functions which have
    some logical connection with a class to the class. '''
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() == rect_2.area():
                return rect_1
            if rect_1.area() > rect_2.area():
                return rect_1
            else:
                return rect_2
