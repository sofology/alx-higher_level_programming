#!/usr/bin/python3


"""Module Base"""

import json
import csv
import turtle


class Base:
    """Base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Init Method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Method for standar format of JSON"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Upload class Base with write a json string"""
        new_list = []
        if list_objs is None:
            return new_list
        else:
            for i in list_objs:
                new_list.append(i.to_dictionary())

        with open("{}.json".format(cls.__name__), "w", encoding='utf-8') as f:
            f.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """Which returns the list of the JSON string representation"""
        if json_string is None or not json_string:
            return "[]"
        
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Method for returns an instance with all the attributes
        already set"""
        if cls.__name__ == "Rectangle":
            inst_fic = cls(123, 456)
        elif cls.__name__ == "Square":
            inst_fic = cls(789)
        inst_fic.update(**dictionary)
        return inst_fic

    @classmethod
    def load_from_file(cls):
        """Return a list of instances"""
        try:
            with open(cls.__name__ + ".json", "r") as f:
                json_string = f.read()
            new_list = cls.from_json_string(json_string)
        except:
            new_list = []

        list_obj = []
        for new_dict in new_list:
            list_obj.append(cls.create(**new_dict))
        return list_obj

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Method for serializes in CSV:"""
        for i in list_objs:
            new_list = i.to_dictionary()
        with open("{}.csv".format(cls.__name__), "w", encoding='utf-8') as f:
            list_key = new_list.keys()
            n_list = csv.DictWriter(f, list_key)
            n_list.writeheader()
            for j in list_objs:
                n_list.writerow(j.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Method for desserializes in CSV"""
        new_list = []
        with open("{}.csv".format(cls.__name__), "r", encoding='utf-8') as f:
            a = csv.DictReader(f)
            for row in a:
                for key, value in row.items():
                    row[key] = int(value)
                new_list.append(cls.create(**row))
        return new_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        gabo = turtle.Screen()
        gabo.bgcolor("grey")
        gabo_turtle = turtle.Turtle()
        gabo_turtle.color("white")

        for a in list_rectangles:
            gabo_turtle.up()
            gabo_turtle.goto(rectangle.x, rectangle.y)
            gabo_turtle.down()
            for b in range(2):
                gabo_turtle.forward(a.width)
                gabo_turtle.left(90)
                gabo_turtle.forward(a.height)
                gabo.left(90)

        for c in list_square:
            gabo_turtle.up()
            gabo_turtle.goto(rectangle.x, rectangle.y)
            gabo.down()
            for c in range(4):
                gabo_turtle.foward(c.width)
                gabo_turtle.left(90)
                gabo_turtle.foward(c.width)
        turtle.done()
