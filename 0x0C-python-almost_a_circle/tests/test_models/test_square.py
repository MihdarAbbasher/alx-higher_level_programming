#!/usr/bin/python3
""" Module for test Square class """
import unittest
from models.square import Square


class TestSquareMethods(unittest.TestCase):
    """ class to test Square class """

    def setUp(self):
        """ Method calles for all tests """
        Square._Base__nb_objects = 0

    def test_id(self):
        """ Test assigned id """
        new = Square(1)
        self.assertEqual(new.size, 1)

    def test_id_default(self):
        """ Test default id """
        new = Square(1, 2)
        self.assertEqual(new.x, 2)

    def test_id_nb_objects(self):
        """ Test nb object attribute """
        new = Square(1, 2, 4)
        self.assertEqual(new.y, 4)

    def test_id(self):
        """test id of inst."""
        new = Square(1, 2, 4, 5)
        self.assertEqual(new.id, 5)
