#!/usr/bin/python3
'''
In this module it's defined a new class "Rectangle" that inherits from Base
'''
from models.base import Base


class Rectangle(Base):
    ''' class Rectangle constructor, using super class's method'''
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
        self.width = width  # callling instance (property) method width
        self.height = height
        self.x = x
        self.y = y

    # width
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w_value):
        if type(w_value) is not int:
            raise TypeError("width must be an integer")
        if w_value <= 0:
            raise ValueError("width must be > 0")
        self.__width = w_value

    # height
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h_value):
        if type(h_value) is not int:
            raise TypeError("height must be an integer")
        if h_value <= 0:
            raise ValueError("height must be > 0")
        self.__height = h_value

    # x variable
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x_value):
        if type(x_value) is not int:
            raise TypeError("x must be an integer")
        if x_value < 0:
            raise ValueError("x must be >= 0")
        self.__x = x_value

    # y variable
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y_value):
        if type(y_value) is not int:
            raise TypeError("y must be an integer")
        if y_value < 0:
            raise ValueError("y must be >= 0")
        self.__y = y_value

    def area(self):
        ''' public instance method that calculates the area of the rectangle
    instantiated '''
        return self.height * self.width

    def display(self):
        ''' prints in stdout the Rectangle instance with the character # '''
        ''' from task 7, it handles x and y variables'''
        for lines in range(self.y):
            print("")
        for row in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def update(self, *args, **kwargs):
        ''' This method that assigns an argument to each attribute
        This type of argument is called a “no-keyword argument”.
        The order in which the arguments are passed is important '''
        if len(args) != 0:
            for arg_num in range(len(args)):
                if arg_num == 0:
                    self.id = args[arg_num]
                elif arg_num == 1:
                    self.width = args[arg_num]
                elif arg_num == 2:
                    self.height = args[arg_num]
                elif arg_num == 3:
                    self.x = args[arg_num]
                elif arg_num == 4:
                    self.y = args[arg_num]
        else:
            for key, value in kwargs.items():
                ''' The items() method returns a view object. The view object
                contains the key-value pairs of the dictionary,
                as tuples in a list.'''
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def __str__(self):
        ''' human-readable string representation for the object or instance '''
        return f'[Rectangle] ({self.id}) {self.x}/{self.y} - \
{self.width}/{self.height}'  # f-strings format

    def to_dictionary(self):
        ''' this public method returns returns the dictionary
        representation of a Rectangle '''
        return {'x': self.x, 'y': self.y
, 'id': self.id, 'height': self.height, 'width': self.width}
