#!/usr/bin/python3
'''
    A function that returns True if the object is an instance of a
class that inherited (directly or indirectly) from the specified
class ; otherwise False.
'''


def inherits_from(obj, a_class):
    ''' Don't get confused between isinstance() and issubclass() as both
methods are quite similar. However, the name itself explains the differences.
isinstance() tests whether the object is an instance or subclass of classinfo.
Whereas, issubclass() only checks if it is a subclass of classinfo or not
(does not check object relationship). '''
    if issubclass(type(obj), a_class) is True:
        return True
    else:
        return False
