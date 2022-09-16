#!/usr/bin/python3
''' You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2
will only be a reference to dict1, and changes made in dict1 will automatically
also be made in dict2. '''


def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    ''' key: new_dict[key] equals to key: value'''
    for key in new_dict:
        new_dict[key] = new_dict[key] * 2
    return new_dict
