#!/usr/bin/python3
""" 1-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print(r1.width) # I added to check that id will be set using the superclass condition, so it sets to the __nb_objects, in this case id
    # wasn't passed, but width and height were(determined by the position of the arguments)
    print(r1.height)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)