#!/usr/bin/python3
class Square:
    """Create Class"""

    def __init__(self, size=0):
        """Create Atribute for Class Square whit Init Method"""
        if type(size) is int:
            self.__size = size
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return(self.__size**2)
