#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
        try:
            for element in range(x):
                print("{}".format(my_list[element]), end="")
            print()
            return element + 1
        except IndexError:
            print()
            return element
