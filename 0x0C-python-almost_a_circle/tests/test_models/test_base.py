#!/usr/bin/python3
"""Base Class test cases"""
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class BaseTest(unittest.TestCase):
    """test cases class"""

    def test_init(self):
        """
        Test initialization of Base class.
        """
        Base._Base__nb_objects = 0
        obj1 = Base()
        obj2 = Base()
        obj3 = Base(12)
        obj4 = Base(-12)
        obj5 = Base("j")
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
        self.assertEqual(obj3.id, 12)
        self.assertEqual(obj4.id, -12)
        self.assertEqual(obj5.id, "j")

    def test_to_json_string(self):
        """
        Test conversion of list of dictionaries to JSON string.
        """
        list_dicts = [{"id": 1}, {"id": 2}, {"id": 3}]
        json_string = Base.to_json_string(list_dicts)
        self.assertEqual(json_string, '[{"id": 1}, {"id": 2}, {"id": 3}]')

        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_from_json_string(self):
        """
        Test loading JSON string and converting it to list of objects.
        """
        json_string = '[{"id": 1}, {"id": 2}]'
        data = Base.from_json_string(json_string)
        self.assertEqual(data, [{"id": 1}, {"id": 2}])

        json_string = None
        data = Base.from_json_string(json_string)
        self.assertEqual(data, [])

    def test_create(self):
        """
        Test creating an object from a dictionary.
        """
        dictionary = {"id": 1, "width": 3, "height": 5, "x": 4, "y": 6}
        rectangle = Base.create(**dictionary)
        self.assertIsInstance(rectangle, Rectangle)
        self.assertEqual(rectangle.id, 1)
        self.assertEqual(rectangle.width, 3)
        self.assertEqual(rectangle.height, 5)
        self.assertEqual(rectangle.x, 4)
        self.assertEqual(rectangle.y, 6)

        dictionary = {"id": 1, "size": 6, "x": 5, "y": 4}
        square = Base.create(**dictionary)
        self.assertIsInstance(square, Square)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 6)
        self.assertEqual(square.x, 5)
        self.assertEqual(square.y, 4)

    def test_save_to_file(self):
        Base._Base__nb_objects = 0

        list_rect = [Rectangle(1, 2), Rectangle(3, 4), Rectangle(5, 6)]
        Rectangle.save_to_file(list_rect)
        with open("Rectangle.json", "r", encoding="utf-8") as file:
            saved_rect = Base.from_json_string(file.read())
        self.assertEqual(
            saved_rect,
            [
                {"id": 1, "width": 1, "height": 2, "x": 0, "y": 0},
                {"id": 2, "width": 3, "height": 4, "x": 0, "y": 0},
                {"id": 3, "width": 5, "height": 6, "x": 0, "y": 0},
            ],
        )

    def test_load_from_file(self):
        Base._Base__nb_objects = 0

        square0 = Square(id=1, size=2, x=3, y=4)
        Square.save_to_file([square0])
        square1 = Square.load_from_file()
        self.assertNotEqual(square1, square0)
        self.assertEqual(len(square1), 1)
        self.assertEqual(square1[0].id, 1)
        self.assertEqual(square1[0].size, 2)
        self.assertEqual(square1[0].x, 3)
        self.assertEqual(square1[0].y, 4)


if __name__ == "__main__":
    unittest.main()
