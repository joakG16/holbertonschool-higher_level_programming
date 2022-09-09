#!/usr/bin/python3
''' startswith will return true when it finds an __
so the condition aply if NOT starts with __'''
''' dir() tries to return a valid list of attributes
of the object it is called upon.'''
if __name__ == '__main__':
    import hidden_4
    listdir = dir(hidden_4)
    for i in listdir:
        if not i.startswith("__", 0):
            print("{}".format(i))
