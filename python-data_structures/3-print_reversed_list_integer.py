#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return None
    my_list.reverse
    for item in reversed(my_list):
        print("{:d}".format(item))
