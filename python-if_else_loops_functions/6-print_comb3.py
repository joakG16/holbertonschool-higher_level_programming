#!/usr/bin/python3
for i in range(0, 9):
    if i == 8:
        print(89)
    else:
        for j in range(i + 1, 10):
            print("{}{}, ".format(i, j), end="")
