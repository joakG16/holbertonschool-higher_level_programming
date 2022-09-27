#!/usr/bin/python3

class MyList(list):
    ''' with list as superclass, this new one
    will inherit its attributes '''

    def print_sorted(self):
        ''' The used function will create a new list containing a 
        sorted version of the list it is given. The sorted()
        function will not modify the list(self) passed as a parameter'''
        print(sorted(self))
