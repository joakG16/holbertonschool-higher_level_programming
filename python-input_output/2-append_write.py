#!/usr/bin/python3
''' a function that appends a string at the end of a text file (UTF8)
and returns the number of characters added '''


def append_write(filename="", text=""):
    ''' creating a file object through open, append(a) mode specified '''
    with open(filename, mode='a', encoding='utf-8') as a_file:
        a_file.write(text)
        return len(text)  # the characters added are in "text" string, so
        # just do a len of text
