#!/usr/bin/python3
''' based on previous task, write a class that raises an exception '''


class BaseGeometry:
    ''' defining method (attrribute)'''
    def area(self):
        raise Exception("area() is not implemented")
