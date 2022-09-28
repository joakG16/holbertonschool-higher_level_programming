#!/usr/bin/python3
''' A function that reads a text file (UTF8) and prints it to stdout '''


def read_file(filename=""):
    ''' open will return a {file object, "file" in this case}, if mode
    is ommited, default is {r}, as for read mode'''
    with open(filename, encoding="utf-8") as file:
        read_data = file.read()  # method that returns some
        # quantity of data and returns a string
        print(read_data, end="")  # end specified since newline from file
        # is also read
