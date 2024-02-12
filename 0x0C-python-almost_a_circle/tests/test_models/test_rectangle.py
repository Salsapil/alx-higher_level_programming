import unittest
from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):

    def test_area(self):
        rect = Rectangle(3, 3)
        self.assertEqual(rect.area(), 9)

    def test_str(self):
        rect = Rectangle(6, 3, 4, 4, 10)
        self.assertEqual(str(rect), "[Rectangle] (10) 4/1 - 6/3")


if __name__ == "__main__":
    unittest.main()
