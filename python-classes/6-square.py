#!/usr/bin/python3
''' Class Square created, used to define a square with respective,
(and optional, zero as default) size as argument passed, that
print respective square, adding an optinal position for this one,
passed through parameter position, later on made private also'''


class Square:
    ''' When an object is created, the __init__() method gets called.
    This method has the line self.size = size.
    This expression automatically calls size(). Same happens
    for self.position'''
    def __init__(self, size=0, position=(0, 0)):  # (width, height)
        self.size = size
        self.position = position

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

    ''' Any code that retrieves the value of position will automatically
    call position() instead of a dictionary (__dict__) look-up, just like
    size attribute'''
    @property
    def position(self):
        return self.__position

    ''' position setter is called even when we create an object. '''
    @position.setter
    def position(self, value):
        if len(value) != 2 or type(value) != tuple:  # checking size/type
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:  # cheking indiv.
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:  # checking for positive/ negative
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    ''' The actual size value is stored in the
    private __size variable. The size *attribute* is a property
    object which provides an interface to this private variable. '''
    def area(self):
        return self.size ** 2

    ''' Print function for square, retrieving the (private) size
    through getter function (size()), if the size is zero it will
    print a blank line only. Added position for square also. '''
    def my_print(self):
        if self.size == 0:
            print()
        else:
            if self.__position[1] > 0:
                for h in range(self.__position[1]):
                    print("")  # for "vertical" position(h), that's why we
                    # don't fill it with spaces, just new lines
            for i in range(self.size):
                for j in range(self.__position[0]):
                    print(" ", end="")  # for "horizontal" position(w), where
                    # spaces are "shown"
                for k in range(self.size):
                    print("#", end="")
                print()
