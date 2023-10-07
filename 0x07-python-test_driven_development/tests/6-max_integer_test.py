#!/usr/bin/python3

"""Unittests for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        orderedli = [1, 2, 3, 4]
        self.assertEqual(max_integer(orderedli), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unorderedli = [1, 2, 4, 3]
        self.assertEqual(max_integer(unorderedli), 4)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [4]
        self.assertEqual(max_integer(one_element), 4)

    def test_floats(self):
        """Test a list of floats."""
        floats = [1.3, 4.353, -95.123, 16.7, 9.0]
        self.assertEqual(max_integer(floats), 16.7)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [1.3, 5.58, -6, 15, 16.6]
        self.assertEqual(max_integer(ints_and_floats), 16.6)

    def test_string(self):
        """Test a string."""
        string = "are hi"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["c", "is", "", "not", "hard"]
        self.assertEqual(max_integer(strings), "not")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
