#!/usr/bin/python3
"""Module"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Square Class """
    def __init__(self, size):
        """Super init for change value width an height for size"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """Return string message"""
        return "[Square] {}/{}".format(self.__size, self.__size)
