#!/usr/bin/python3
''' this module will replace with two new lines each time
it finds a symbol which can be either "." ":" or "?",
and no whitespace is found at the beggining of each printed
line, as specified to replace that space in the function below'''


def text_indentation(text):
    ''' check if text passed is type str'''
    if type(text) is not str:
        raise TypeError("text must be a string")

    after_new_line = False
    for char in text:
        if after_new_line:
            if char == " ":  # if there was a space after the new line printed
                continue
            after_new_line = False
        if char == '.' or char == '?' or char == ':':
            print(char)
            print()
            after_new_line = True  # after sym. found, there could be a space
        else:
            print(char, end="")  # keep printing other symbols
