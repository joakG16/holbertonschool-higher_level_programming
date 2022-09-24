#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Creating/defining TestMaxInteger class"""

    def type_error_list(self):
        '''string in between'''
        with self.assertRaises(TypeError):
            max_integer([4, 'error', 3, 6])

    def test2(self):
        ''' None '''
        self.assertRaises(TypeError, max_integer, None)

    def test3(self):
        ''' Float '''
        self.assertEqual(max_integer([7.7]), 7.7)

    def test4(self):
        ''' Same number '''
        self.assertEqual(max_integer([7, 7, 7, 7, 7]), 7)

    def test5(self):
        ''' Negatives '''
        self.assertEqual(max_integer([-7, -9, 2, 37, -44, 52]), 52)
    
    def test5(self):
        ''' Empty list '''
        self.assertEqual(max_integer([]), None)


if __name__ == '__main__':
    unittest.main()
