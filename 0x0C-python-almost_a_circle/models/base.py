#!/usr/bin/python3
"""module"""
import json
import csv


class Base:
    """super class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """__init__"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """class method"""
        file_name = cls.__name__ + ".json"
        with open(file_name, "w+", encoding="utf-8") as file:
            if list_objs is not None:
                json_data = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(json_data))
            else:
                file.write(Base.to_json_string([]))

    @staticmethod
    def from_json_string(json_string):
        """static method"""
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """class method"""
        from models.rectangle import Rectangle
        from models.square import Square
        if "size" in dictionary.keys():
            square = Square(size=1)
            square.update(**dictionary)
            return square

        rect = Rectangle(width=1, height=1)
        rect.update(**dictionary)
        return rect

    @classmethod
    def load_from_file(cls):
        """class method"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = file.read()
                list_dicts = cls.from_json_string(data)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """class method"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([obj.id, obj.width,
                                    obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """class method"""
        filename = cls.__name__ + ".csv"
        with open(filename, "r") as file:
            reader = csv.reader(file)
            if reader:
                instances = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        instance = cls.create(
                            id=int(row[0]), width=int(row[1]),
                            height=int(row[2]), x=int(row[3]), y=int(row[4])
                            )
                    elif cls.__name__ == "Square":
                        instance = cls.create(
                            id=int(row[0]), size=int(row[1]),
                            x=int(row[2]), y=int(row[3])
                            )
                    instances.append(instance)
                return instances
            else:
                return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draws our shapes"""
        from turtle import Turtle
        import turtle
        tr = Turtle()
        tr.speed(1)
        tr.shapesize(1)
        tr.color('#d3687f')
        tr.shape('turtle')
        tr.fillcolor("#D6ED17")
        tr.width(1)
        for rect in list_rectangles:
            tr.setpos(rect.x, rect.y)
            tr.pendown()
            tr.forward(rect.width)
            tr.right(90)
            tr.forward(rect.height)
            tr.right(90)
            tr.forward(rect.width)
            tr.right(90)
            tr.forward(rect.height)
            tr.right(90)
            tr.penup()
        tr.color('#D6ED17')
        tr.fillcolor("#d3687f")
        for sqr in list_squares:
            tr.setpos(sqr.x, sqr.y)
            tr.pendown()
            tr.backward(sqr.size)
            tr.right(90)
            tr.backward(sqr.size)
            tr.right(90)
            tr.backward(sqr.size)
            tr.right(90)
            tr.backward(sqr.size)
            tr.right(90)
            tr.penup()
        tr.hideturtle()
        turtle.done()
