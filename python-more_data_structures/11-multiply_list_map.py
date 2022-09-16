#!/usr/bin/python3


def multiply_list_map(my_list=[], number=0):
    copy_list = my_list.copy()
    copy_list = list(map(lambda value: value * number, copy_list))
    return copy_list