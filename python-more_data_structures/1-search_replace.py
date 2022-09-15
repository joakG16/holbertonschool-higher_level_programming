#!/usr/bin/python3
''' this function will populate the list from test with replace if condition
is true, else will populte it with value'''


def search_replace(my_list, search, replace):
        return [replace if value == search else value for value in my_list]
