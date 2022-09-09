#!/usr/bin/python3

from sys import argv


if __name__ == '__main__':
    import sys
    argsum = 0
    for i in range(1, len(sys.argv)):
        argsum = argsum + int(argv[i])
    print("{}".format(argsum))
