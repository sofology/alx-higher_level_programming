#!/usr/bin/python3
class Square:
    """Create Class"""

    def __init__(self, size=0, position=(0, 0)):
        """Create Atribute for Class Square whit Init Method"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Exception Error"""
        mesg_err = "position must be a tuple of 2 positive integers"
        if type(value) is tuple:
            if len(value) is not 2:
                raise TypeError(mesg_err)
            else:
                for a in range(len(value)):
                    if value[a] < 0:
                        raise TypeError(mesg_err)
            self.__position = value
        else:
            raise TypeError(mesg_err)

    def area(self):
        """Function for find the area square"""
        return(self.__size**2)

    def my_print(self):
        """function for print square"""
        if self.size is 0:
            print('')
        else:
            for a in range(self.__position[1]):
                print('')
            for colums in range(self.__size):
                for lines in range(self.size + self.__position[0]):
                    if lines < self.__position[0]:
                        print(" ", end='')
                    else:
                        print("#", end='')
                print('')
