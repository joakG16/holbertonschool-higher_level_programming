#!/usr/bin/python3
''' Writing a class Square '''


class Square:
    ''' Private instantiation through method'''
    def __init__(self, size=0):
        self.set_size(size)
    
    # size setter
    def set_size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
