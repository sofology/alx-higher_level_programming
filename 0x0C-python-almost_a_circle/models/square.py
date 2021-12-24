#!/usr/bin/python3


"""Module Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Method init for constructor class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Method size"""
        return self.width

    @size.setter
    def size(self, size):
        """Method Setter for validate size value"""
        if type(size) is not int:
            raise TypeError("width must be an integer")
        elif size <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = size
            self.height = size

    def __str__(self):
        """Method fot anulate __str__"""
        return("[Square] ({}) {}/{} - {}".format(self.id,
               self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """Method for update class square with *args **kwargs"""
        new_list = ['id', 'size', 'x', 'y']
        new_dict = {'id': 'id', 'width': '_Rectangle__width', 'height':
                    '_Rectangle__height', 'x': '_Rectangle__x', 'y':
                    '_Rectangle__y'}

        for num, val in enumerate(args):
            if num != 1:
                self.__dict__[new_dict[new_list[num]]] = val
            else:
                self.height = val
                self.width = val

        if len(args) == 0:
            for key, value in kwargs.items():
                if key != "size":
                    self.__dict__[new_dict[key]] = value
                else:
                    self.height = value
                    self.width = value

    def to_dictionary(self):
        """Method for return square dictionary"""
        nw_dict = Rectangle.to_dictionary(self)
        nw_dict["size"] = nw_dict["width"]
        del nw_dict["height"]
        del nw_dict["width"]
        return nw_dict
