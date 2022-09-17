#!/usr/bin/python3


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        ''' if print cause of value falls into error, return line won't be executed '''
        return True
    except (ValueError, TypeError):
        return False
