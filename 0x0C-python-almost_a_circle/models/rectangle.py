#!/usr/bin/python3

"""Module Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor Class Method Init"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """Method for calculate area"""
        return self.__width * self.__height

    def display(self):
        """Method for display a accsi character"""
        print("\n" * self.__y, end='')
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        """Method for assigns an argument to each attribute"""
        new_list = ['id', 'width', 'height', 'x', 'y']
        if args:
            for i, j in enumerate(args):
                setattr(self, new_list[i], j)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)


    def __str__(self):
        """Metod for anulate __str__"""
        a = "Rectangle"
        b = self.id
        c = self.__x
        d = self.__y
        e = self.__width
        f = self.__height
        return("[{}] ({}) {}/{} - {}/{}".format(a, b, c, d, e, f))

    @property
    def width(self):
        """Method width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Method Setter for validate value width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """Method height"""
        return self.__width

    @height.setter
    def height(self, height):
        """Method Setter for validate value height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """Method x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Method setter for validate value x"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """Method y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Method setter for validate value y"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def to_dictionary(self):
        """Method for return rectangle dictionary"""
        new_dict = {'id': 'id', 'width': '_Rectangle__width', 'height':
                    '_Rectangle__height', 'x': '_Rectangle__x', 'y':
                    '_Rectangle__y'}

        nw_dic = {}
        for key, value in new_dict.items():
            nw_dic[key] = self.__dict__[value]
        return nw_dic
