#!/usr/bin/python3
""" Unittest for rectangle class """

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    ''' testing class '''
    def test_rect1(self):
        ''' passing width and height'''
        A1 = Rectangle(1, 2)
        self.assertEqual(A1.__str__(), '[Rectangle] (1) 0/0 - 1/2')
        #       [ClassType] (id) x/y - width/height

    def test_rect2(self):
        ''' passing width, height and x '''
        B1 = Rectangle(1, 2, 3)
        self.assertEqual(B1.__str__(), '[Rectangle] (2) 3/0 - 1/2')

    def test_rect3(self):
        ''' string passed as y error'''
        with self.assertRaises(TypeError):
            C1 = Rectangle(1, 2, 3, "4")


if __name__ == '__main__':
    unittest.main()
