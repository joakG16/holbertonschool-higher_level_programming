#!/usr/bin/pyhton3


def uniq_add(my_list=[]):
    ''' Set only stores a value once even if
    it is inserted more than once. '''
    set_list = set(my_list)
    unique_list = (list(set_list))
    res = 0
    for x in unique_list:
        res = res + x
    return res
    