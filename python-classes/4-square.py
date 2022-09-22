#!/usr/bin/python3
''' Class Square created, used to define a square with respective,
size as argument passed, later on to be private to ensure
type/validation and how it will be retrieved from outside, done
by using the property attribute. '''


class Square:
    ''' When an object is created, the __init__() method gets called.
    This method has the line self.size = size.
    This expression automatically calls size().'''
    def __init__(self, size=0):
        self.size = size  # self.propertyobject = argument passed (size)

    ''' Simply put, property attaches some code (getter and setter)
    to the member attribute accesses (size). '''
    ''' Any code that retrieves the value of size will automatically
    call size() instead of a dictionary (__dict__) look-up. '''
    @property
    def size(self):
        return self.__size

    ''' size is called even when we create an object. '''
    @size.setter
    def size(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    ''' The actual size value is stored in the
    private __size variable. The size *attribute* is a property
    object which provides an interface to this private variable. '''
    def area(self):
        return self.size ** 2
