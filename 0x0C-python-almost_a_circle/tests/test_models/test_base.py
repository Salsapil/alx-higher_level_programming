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
        data = [{"id": "1", "id": 2}]
        json_string = Base.to_json_string(data)
        self.assertEqual(json_string, '[{"id": "1", "id": 2}]')

        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_save_to_file(self):
        """
        Test saving a list of objects to JSON file.
        """
        b1 = Base(1)
        b2 = Base(2)
        data = [b1, b2]
        Base.save_to_file(data)

        with open("Base.json", "r") as file:
            content = file.read()
        expected_content = '[{"id": 1}, {"id": 2}]'
        self.assertEqual(content, expected_content)

        # Cleanup
        import os
        os.remove("Base.json")

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

    def test_load_from_file(self):
        """
        Test loading objects from JSON file.
        """
        b1 = Base(1)
        b2 = Base(2)
        data = [b1, b2]
        Base.save_to_file(data)

        loaded_data = Base.load_from_file()
        self.assertEqual(loaded_data, [{"id": 1}, {"id": 2}])
