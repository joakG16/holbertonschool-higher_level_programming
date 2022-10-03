#!/usr/bin/python3
'''
In this module it's defined a new class "Rectangle" that inherits from Base
'''
from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' Call the super class with id - this super call with use
        the logic of the __init__ of the Base class
        '''
        super().__init__(id)

        '''
        Why private attributes with getter/setter?
        Why not directly public attribute?

        Because we want to protect attributes of our class.
        With a setter, you are able to validate what a developer
        is trying to assign to a variable. So after, in your class
        you can “trust” these attributes.
        '''
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w_value):
        self.__width = w_value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h_value):
        self.__height = h_value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x_value):
        self.__x = x_value

    @property
    def y(self):
        return self.__y

    @x.setter
    def y(self, y_value):
        self.__y = y_value
