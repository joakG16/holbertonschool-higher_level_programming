#!/usr/bin/python3
''' writing a class with respective attributes descripted inside '''

class BaseGeometry:
    ''' defining method for non-implemented area '''
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        ''' creating a field (name variable)'''
        self.name = name
        ''' public instance method for type checking'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(self.name))
        ''' public intance method for value checking '''
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
