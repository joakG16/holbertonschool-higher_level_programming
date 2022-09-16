#!/usr/bin/python3
''' The update() method will update the dictionary with the items from a given
argument. If the item does not exist, the item will be added. '''


def update_dictionary(a_dictionary, key, value):
    update_dic = a_dictionary
    update_dic.update({key: value})
    return update_dic
