#!/usr/bin/python3
""" Module that contains class Base """
import json

class Base:
    """ Class Base as base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Method to initializes instances"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    @staticmethod
    def to_json_string(list_dictionaries):
        """ Convert list to JSON string """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

