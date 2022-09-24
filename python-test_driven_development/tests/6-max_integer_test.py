#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Creating/defining TestMaxInteger class"""

    def test1(self):
        with self.assertRaises(TypeError):
            max_integer(['tati', 7, 9, 2])

    def test2(self):
        self.assertEqual(max_integer([]), None)

    def test3(self):
        self.assertEqual(max_integer([7, 9, 2, 37, 44, 52]), 52)

    def test4(self):
        self.assertEqual(max_integer([7, 7, 7, 7, 7]), 7)

    def test5(self):
        self.assertEqual(max_integer([-7, -9, 2, 37, -44, 52]), 52)


if __name__ == '__main__':
    unittest.main()
