#!/usr/bin/python3
''' Class Square created, used to define a square with respective,
size as argument passed, and print respective square. '''


class Square:
    ''' When an object is created, the __init__() method gets called.
    This method has the line self.size = size.
    This expression automatically calls size().'''
    def __init__(self, size=0):
        self.size = size

    ''' Any code that retrieves the value of size will automatically
    call size() instead of a dictionary (__dict__) look-up. '''
    @property
    def size(self):
        return self.__size

    ''' size setter is called even when we create an object. '''
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

    ''' Print function for square, retrieving the (private) size
    through getter function (size()), if the size is zero it will
    print a blank line only. '''
    def my_print(self):
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print()
