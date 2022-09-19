#!/usr/bin/python3


def roman_to_int(roman_string):

    if not isinstance(roman_string, str) or not roman_string:
        return 0

    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    number = 0

    ''' multiple replace of "border cases", to later sum in "number" '''
    roman_string = roman_string.replace("IV", "IIII").replace("IX", "VIIII")
    roman_string = roman_string.replace("XL", "XXXX").replace("XC", "LXXXX")
    roman_string = roman_string.replace("CD", "CCCC").replace("CM", "DCCCC")

    for letter in roman_string:
        '''r_dict[letter] is r_dict["X"](exam.), gets value of "X" = 10'''
        number += roman_dict[letter]
    return number
