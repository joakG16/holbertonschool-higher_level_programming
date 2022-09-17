#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
            for element in range(x):
                try:
                    print("{}".format(my_list[element]), end="")
                except IndexError:
                    print()
                    return element
            print()
            return element + 1
