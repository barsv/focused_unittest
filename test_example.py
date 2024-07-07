# test_example.py
import unittest
from focused_unittest import FocusedTestCase, focus

class TestExample(FocusedTestCase):

    @focus
    def test_add(self):
        self.assertEqual(2 + 3, 5)

    @focus
    def test_subtract(self):
        self.assertEqual(3 - 2, 1)

    def test_multiply(self):
        self.assertEqual(3 * 2, 6)

    def test_divide(self):
        self.assertEqual(6 / 2, 3)

if __name__ == '__main__':
    unittest.main()
