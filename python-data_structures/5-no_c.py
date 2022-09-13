#!/usr/bin/python3


def no_c(my_string):
    no_c_str = '' ''' defining a new string, since they are inmutable '''
    for ch in my_string:
        ''' append the ch according to the condition '''
        if ch == 'c' or ch == 'C':
            no_c_str += ''
        else:
            no_c_str += ch
    return no_c_str
