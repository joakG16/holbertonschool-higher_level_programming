#!/usr/bin/python3
'''
In this module it's defined a new class "Square" that inherits from Rectangle
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' A Square is a special Rectangle, so it makes sense this class Square
    inherits from Rectangle. Now you have a Square class who has the same
    attributes and same methods.'''
    def __init__(self, size, x=0, y=0, id=None):
        ''' This super call will use the logic of the __init__ of the Rectangle
        class. The width and height must be assigned to the value of size '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        ''' string rep. of a square '''
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'

    @property
    def size(self):
        ''' getter using property method from superclass '''
        return self.width

    @size.setter
    def size(self, size_value):
        ''' getter using setter property methods from superclass '''
        self.width = size_value
        self.height = size_value
        
    def update(self, *args, **kwargs):
        ''' This method assigns an argument to each specified in
        order to update the instance's attribute.
        This type of argument is called a “no-keyword argument”.
        The order in which the arguments are passed is important '''
        if args and len(args) != 0:
            for arg_num in range(len(args)):
                if arg_num == 0:
                    self.id = args[arg_num]
                elif arg_num == 1:
                    self.size = args[arg_num]
                elif arg_num == 2:
                    self.x = args[arg_num]
                elif arg_num == 3:
                    self.y = args[arg_num]
        else:
            for key, value in kwargs.items():
                ''' The items() method returns a view object. The view object
                contains the key-value pairs of the dictionary,
                as tuples in a list.'''
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.width = value
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
