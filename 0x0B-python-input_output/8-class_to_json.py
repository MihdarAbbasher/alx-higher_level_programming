#!/usr/bin/python3

"""Defines a Python class to JSON dict. function."""


def class_to_json(obj):
    """Returns the dictionary representation of simple data structure."""
    return obj.__dict__
