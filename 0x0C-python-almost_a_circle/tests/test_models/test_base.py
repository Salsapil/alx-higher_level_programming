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
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(10)
        self.assertEqual(b2.id, 10)
        b3 = Base(-12)
        self.assertEqual(b3.id, -12)
        b4 = Base("j")
        self.assertEqual(b4.id, "j")

    def test_nb_objects(self):
        """
        Test automatic id generation and nb_objects counter.
        """
        self.assertEqual(Base.__nb_objects, 0)
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(Base.__nb_objects, 2)

    def test_to_json_string(self):
        """
        Test conversion of list of dictionaries to JSON string.
        """
        data = [{"key1": "value1", "key2": 2}]
        json_string = Base.to_json_string(data)
        self.assertEqual(json_string, '[{"key1": "value1", "key2": 2}]')

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
        data = {"id": 3, "property1": "value1"}
        b = Base.create(**data)
        self.assertEqual(b.id, 3)
        self.assertEqual(b.property1, "value1")

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

        # Cleanup
        import os
        os.remove("Base.json")

    def test_save_to_file_csv(self):
        """
        Test saving a list of rectangles to CSV file.
        """
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(5, 6, 7, 8)
        data = [r1, r2]
        Base.save_to_file_csv(data)

        with open("Rectangle.csv", "r") as file:
            content = file.read()
        expected_content = "1,2,3,4\n5,6,7,8\n"
        self.assertEqual(content, expected_content)

        # Cleanup
        import os
        os.remove("Rectangle.csv")
