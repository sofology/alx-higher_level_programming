#!/usr/bin/python3
class Square:
    """Create Class"""

    def __init__(self, size=0):
        """Create Atribute for Class Square whit Init Method"""
        self.size = size

    @property
    def size(self):
        """size"""
        return self.__size

    @size.setter
    def size(self, value):
        """"Exception Error"""
        if type(value) is int:
            self.__size = value
            if value < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Function for find the area square"""
        return(self.__size**2)

    def my_print(self):
        """function for print square"""
        if self.size is 0:
            print()
        for row in range(self.__size):
            for columns in range(self.__size):
                print("#", end='')
            print()
