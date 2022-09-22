#!/usr/bin/python3
''' Writing a class Square '''


class Square:
    '''instantiation of size attribute'''
    def __init__(self, size=0):
        self.set_size(size)

    # size setter used in instantiation (value is size passed as argument)
    def set_size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    ''' public instance method that calculates the area of given size '''
    def area(self):
        return self.__size ** 2
