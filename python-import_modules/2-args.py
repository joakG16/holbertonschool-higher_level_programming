#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    len_a = len(sys.argv)
    op1 = "argument"
    op2 = "arguments"

    if len_a < 2:
        print("0 arguments.")
    else:
        print("{0}: {1}".format(len_a - 1, op1 if (len_a == 2) else op2))
        for i in range(1, len_a):
            print("{0}: {1}".format(i, sys.argv[i]))
