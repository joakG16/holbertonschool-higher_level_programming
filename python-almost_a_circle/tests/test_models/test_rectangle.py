#!/usr/bin/python3
"""Module Test Class Rectangle"""


import unittest
from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Testing Rectangle"""
    def test_exists(self):
        rec = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rec.id, 5)

    def test_arearect_str_dic(self):
        self.r1 = Rectangle(1, 2)
        self.assertEqual(self.r1.area(), 2)
        self.assertEqual(self.r1.__str__(), '[Rectangle] (17) 0/0 - 1/2')
        self.assertEqual(self.r1.to_dictionary(), {'id': 17, 'width': 1, 'height': 2, 'x': 0, 'y': 0})

    def test_rect_err(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_disp(self):
        r3 = Rectangle(1, 1, 0, 0)
        with patch('sys.stdout', new=StringIO()) as outp:
            r3.display()
        self.assertEqual(outp.getvalue(), '#\n')
        r4 = Rectangle(1, 2, 0, 1, 2)
        with patch('sys.stdout', new=StringIO()) as out4:
            r4.display()
        self.assertEqual(out4.getvalue(), '\n#\n#\n')

    def test_nice_update(self):
        r5 = Rectangle(3, 6)
        r5.update(6, 9)
        self.assertEqual(r5.__str__(), '[Rectangle] (6) 0/0 - 9/6')
        r6 = Rectangle(1, 2, 0, 1, 2)
        r6.update(**{ 'id': 89, 'x': -1})
        self.assertEqual(r6.__str__(), '[Rectangle] (89) -1/1 - 1/2')
        r7 = Rectangle(3, 2, 1)
        r7.update("facubo7", None, None)
        self.assertEqual(r7.__str__(), '[Rectangle] (facubo7) 1/0 - None/None')
        r8 = Rectangle(6, 4, id="nice")
        r8.update(None)
        self.assertEqual(r8.__str__(), '[Rectangle] (nice) 0/0 - 6/4')

    def test_creation(self):
        cre = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 })
        self.assertEqual(cre.__str__(), '[Rectangle] (89) 3/4 - 1/2')

    def test_savetofilerec(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as fp:
            self.assertEqual('[]', fp.read())
        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json") as fp3:
            self.assertEqual(fp3.read(), '[{"id": 24, "width": 1, "height": 2, "x": 0, "y": 0}]')

    def test_loadfromfilerec(self):
        Rectangle.save_to_file([Rectangle(1, 2)])
        lf = Rectangle.load_from_file()
        self.assertTrue(isinstance(lf, list))

class TestChori(unittest.TestCase):
    def test_saveempty(self):
        emlii = []
        Rectangle.save_to_file(emlii)
        with open("Rectangle.json") as p:
            self.assertEqual('[]', p.read())

if __name__ == '__main__':
    unittest.main()
