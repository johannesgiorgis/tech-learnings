"""
Test Mock Demo
"""

import unittest
from unittest.mock import patch


class ClassA:
    """Class to illustrate use of patch objects"""

    def __init__(self, data):
        self.data = data

    def get_data(self):
        return self.data


class TestClassA(unittest.TestCase):
    """Unittest class for testing ClassA

    This is a trivial example.
    """

    a = ClassA(100.0)

    def test_get_data(self):
        """unit test for ClassA.get_data"""
        with patch.object(a, "data", new=200.0):
            self.assertEqual(200.0, a.get_data())


if __name__ == "__main__":
    unittest.main()
