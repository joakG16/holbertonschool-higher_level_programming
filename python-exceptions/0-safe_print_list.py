#!/usr/bin/python3
''' range(x) goes from 0 to x - 1, remember '''


def safe_print_list(my_list=[], x=0):
        element = 0
        for element in range(x):
            try:
                print("{}".format(my_list[element]), end="")
                ''' the next line it's just for the return value, because element
                will be restarted to keep with the sequence established on the range'''
                element += 1
            except IndexError:
                break
        print()
        return element
