#!/usr/bin/python3
''' this module will replace with two new lines each time
it finds a symbol which can be either "." ":" or "?",
and no whitespace is found at the beggining of each printed
line, as specified to replace that space in the function below'''


def text_indentation(text):
    ''' check if text passed is type str'''
    if type(text) is not str:
        raise TypeError("text must be a string")

    '''replacing characters'''
    replaced_text = text.replace(". ", ".\n\n")\
        .replace("? ", "?\n\n").replace(": ", ":\n\n")
    print(replaced_text)
        