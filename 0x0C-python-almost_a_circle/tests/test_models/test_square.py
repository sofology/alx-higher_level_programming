#!/usr/bin/python3


""" Module to test rectangle """


import unittest
import pep8
from models.square import Square


class format_pep8(unittest.TestCase):
    """Class for check pep8 """
    def test_pep8_rec(self):
        """Method for check the pep8 """
        checker = pep8.Checker("models/square.py", show_source=True)
        file_error = checker.check_all()


class Test_Square(unittest.TestCase):
    """Class to test the square file """

    def setUp(self):
        """ Method for check attributes"""
        self.r1 = Square(10, 2)
        self.r2 = Square(2, 10)

    def tearDown(self):
        """Method for test to restart a process """
        pass

    def test_id(self):
        """Method for test the id attribute"""
        self.assertEqual(self.r1.id, 15)
        self.assertEqual(self.r2.id, 16)

    def test_size(self):
        """Method for test height attribute"""
        self.assertEqual(self.r1.size, 10)
        self.assertEqual(self.r2.size, 2)

    def test_x(self):
        """Method for test the x attribute"""
        self.assertEqual(self.r1.x, 2)
        self.assertEqual(self.r2.x, 10)

    def test_y(self):
        """Method for test the y attribute"""
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r2.y, 0)

if __name__ == "__main__":
    unittest.main()
