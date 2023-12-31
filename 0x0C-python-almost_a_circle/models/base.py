#!/usr/bin/python3
""" Module that contains class Base """

import json
import csv
import os.path


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

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save object into a file """
        filename = "{}.json".format(cls.__name__)
        list_dic = []
        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                list_dic.append(list_objs[i].to_dictionary())
        lists = cls.to_json_string(list_dic)
        with open(filename, 'w') as f:
            f.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """ Convert JSON string into dictionary """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Create an instance """
        if cls.__name__ == "Rectangle":
            new = cls(10, 10)
        else:
            new = cls(10)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file_csv(cls):
        """ Returns a list of instances from file"""
        filename = "{}.csv".format(cls.__name__)
        if os.path.exists(filename) is False:
            return []
        with open(filename, 'r') as f:
            list_str = f.read()
        list_inst = cls.from_json_string(list_str)
        for x in list_inst:
            print("-------------------------\nx:")
            print(x)
            list_inst.append(x)
        return list_inst

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Saves data to csv file """
        filename = "{}.csv".format(cls.__name__)

        if cls.__name__ == "Rectangle":
            list_dic = [0, 0, 0, 0, 0]
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_dic = ['0', '0', '0', '0']
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        if not list_objs:
            pass
        else:
            for obj in list_objs:
                for kv in range(len(list_keys)):
                    list_dic[kv] = obj.to_dictionary()[list_keys[kv]]
                matrix.append(list_dic[:])

        with open(filename, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(matrix)
