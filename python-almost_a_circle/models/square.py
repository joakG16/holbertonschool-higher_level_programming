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
