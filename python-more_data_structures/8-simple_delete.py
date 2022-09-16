#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    if a_dictionary.get(key) is None:
        return a_dictionary
    else:
        update_dic = a_dictionary
        update_dic.pop(key)
        return update_dic
