#!/usr/bin/python3


""" Module to test rectangle """


import unittest
import pep8
from models.rectangle import Rectangle


class format_pep8(unittest.TestCase):
    """Class for check pep8 """
    def test_pep8_rec(self):
        """Method for check the pep8 """
        checker = pep8.Checker("models/rectangle.py", show_source=True)
        file_error = checker.check_all()


class Test_Rectangle(unittest.TestCase):
    """Class to test the rectangle file """

    def setUp(self):
        """ Method for check attributes"""
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(2, 10)
        self.r3 = Rectangle(10, 2, 0, 0, 12)

    def tearDown(self):
        """Method for test to restart a process """
        pass

    def test_id(self):
        """Method for test the id attribute"""
        self.assertEqual(self.r1.id, 7)
        self.assertEqual(self.r2.id, 8)
        self.assertEqual(self.r3.id, 12)

    def test_width(self):
        """Method for test width attribute"""
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r3.width, 10)

    def test_height(self):
        """Method for test height attribute"""
        self.assertEqual(self.r1.height, 10)
        self.assertEqual(self.r2.height, 2)
        self.assertEqual(self.r3.height, 10)

    def test_x(self):
        """Method for test the x attribute"""
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r2.x, 0)
        self.assertEqual(self.r3.x, 0)

    def test_y(self):
        """Method for test the y attribute"""
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r2.y, 0)
        self.assertEqual(self.r3.y, 0)

if __name__ == "__main__":
    unittest.main()
