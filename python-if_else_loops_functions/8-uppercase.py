#!/usr/bin/python3
islower = __import__('7-islower').islower


def uppercase(str):
    newstring = ''
    for a in str:
        if islower(a) is True:
            newstring += (chr(ord(a) - 32))
        else:
            newstring += a
    print("{}".format(newstring))
