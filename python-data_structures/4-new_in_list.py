#!/usr/bin/python3

from http.client import FOUND


def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        return my_list.copy()
    list_copy = my_list.copy()
    for item in range(len(list_copy)):
        if list_copy[item] == idx:
            list_copy[item] == element
            print(item)
            return list_copy
