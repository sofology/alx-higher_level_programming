#!/usr/bin/python3
"""Module"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Square Class """
    def __init__(self, size):
        """Muper init for change value width an height for size"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(self.__size, self.__size)
