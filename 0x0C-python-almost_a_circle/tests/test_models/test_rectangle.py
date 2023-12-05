#!/usr/bin/python3
""" Module for test Rectangle class """
import unittest
from models.rectangle import Rectangle


class TestRectangleMethods(unittest.TestCase):
    """ class to test Rectangle class """

    def setUp(self):
        """ Method calles for all tests """
        Rectangle._Base__nb_objects = 0

    def test_id(self):
        """ Test assigned id """
        new = Rectangle(1, 2)
        self.assertEqual(new.width, 1)
        self.assertEqual(new.height, 2)

    def test_id_default(self):
        """ Test default id """
        new = Rectangle(1, 2, 3)
        self.assertEqual(new.x, 3)

    def test_id_nb_objects(self):
        """ Test nb object attribute """
        new = Rectangle(1, 2, 3, 4)
        self.assertEqual(new.y, 4)

    def test_id(self):
        """test id of inst."""
        new = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(new.id, 5)
