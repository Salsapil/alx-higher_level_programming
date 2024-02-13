import unittest
from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):

    def test_area(self):
        rect = Rectangle(3, 3)
        self.assertEqual(rect.area(), 9)


if __name__ == "__main__":
    unittest.main()
