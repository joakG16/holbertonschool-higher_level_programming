#!/usr/bin/python3
""" Unit Test for Base Class """

import unittest
from models.base import Base


class TestClass(unittest.TestCase):
    """Base class tests"""
    def test_validate(self):
        """ validate the id number, without args """
        A1 = Base()
        self.assertEqual(A1.id, 1)

    def test_validate1(self):
        """ validate the id number, with args """
        B1 = Base(89)
        self.assertEqual(B1.id, 89)
        B2 = Base(-13)
        self.assertEqual(B2.id, -13)

    def test_validate2(self):
        """ validate the id number, with 2 or more args"""
        with self.assertRaises(TypeError):
            C1 = Base(3, 7)

    def test_validate3(self):
        ''' should assign correct id '''
        D1 = Base()
        D2 = Base()
        self.assertEqual(D2.id, 3)

    def test_validate4(self):
        ''' should return an empty list '''
        E1 = Base.to_json_string(None)
        self.assertEqual(E1, "[]")

    def test_validate5(self):
        ''' should return an empty list '''
        F1 = Base.to_json_string([])
        self.assertEqual(F1, "[]")

    def test_validate6(self):
        ''' should return a JSON string '''
        G1 = Base.to_json_string([{'id': 12}])
        self.assertEqual(G1, '[{"id": 12}]')

    def test_validate7(self):
        ''' should return an empty list '''
        H1 = Base.from_json_string(None)
        self.assertEqual(H1, [])

    def test_validate8(self):
        ''' should return an empty list '''
        I1 = Base.from_json_string("[]")
        self.assertEqual(I1, [])

    def test_validate9(self):
        ''' should return a list '''
        J1 = Base.from_json_string('[{ "id": 89 }]')
        self.assertEqual(J1, [{'id': 89}])


if __name__ == "__main__":
    unittest.main()
