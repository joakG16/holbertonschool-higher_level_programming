#!/usr/bin/python3
''' A function that writes a string to a text file (UTF8) and
returns the number of characters written '''


def write_file(filename="", text=""):
    ''' creating a file object through open, append mode specified '''
    with open(filename, mode='a', encoding='utf-8') as file:
        file.write(text)
        return file.tell()  # The tell() method returns the current
        # file position in a file stream.
