#!/usr/bin/python3
from ast import Sub
from audioop import mul
from re import M, sub


if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    print("{0} + {1} = {2}".format(a, b, add(a, b)))
    print("{0} - {1} = {2}".format(a, b, sub(a, b)))
    print("{0} * {1} = {2}".format(a, b, mul(a, b)))
    print("{0} / {1} = {2}".format(a, b, div(a, b)))
