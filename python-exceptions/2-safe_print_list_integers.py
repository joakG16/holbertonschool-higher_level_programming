#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    for element in range(x):
        try:
            print("{:d}".format(my_list[element]), end="")
            element += 1
        except (ValueError, TypeError):
            ''' next line is for return value, so it doesn't count the
            index in which the last error ocurred, and print real number of
            int printed'''
            element -= 1
            continue
    print()
    return element
