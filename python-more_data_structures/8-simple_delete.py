#!/usr/bin/python3
''' first it will be checked if the key is present, if it is,
the pop method will remove it along with it's value'''

def simple_delete(a_dictionary, key=""):
    if a_dictionary.get(key) is None:
        return a_dictionary
    else:
        update_dic = a_dictionary
        update_dic.pop(key)
        return update_dic
