#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    index, count = 0, 0
    while index < x:
        try:
            print("{:d}".format(my_list[index]), end="")
            index += 1; count += 1
        except (ValueError, TypeError):
            ''' index will change, but not count because, as an error
            it won't be printed'''
            index += 1
            continue
    print()
    return count
