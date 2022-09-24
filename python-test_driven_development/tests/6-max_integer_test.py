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

    def test1(self):
        ''' None '''
        self.assertRaises(TypeError, max_integer, None)

    def test2(self):
        ''' max at the end '''
        self.assertEqual(max_integer([1, 2, 7]), 7)

    def test3(self):
        ''' max at the beginning '''
        self.assertEqual(max_integer([7, 3, 2, 4, 1]), 7)

    def test4(self):
        ''' max in the middle '''
        self.assertEqual(max_integer([2, 4, 8, 5, 3]), 8)
        
    def test5(self):
        ''' one negative number '''
        self.assertEqual(max_integer([-7, 9, 2, 37, 44, 52]), 52)
    
    def test6(self):
        ''' only negatives '''
        self.assertEqual(max_integer([-7, -9, -2, -37, -44, -52]), -2)
    
    def test7(self):
        ''' Empty list '''
        self.assertEqual(max_integer([]), None)


if __name__ == '__main__':
    unittest.main()
