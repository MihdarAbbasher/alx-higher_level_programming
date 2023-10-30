#!/usr/bin/python3

"""Defines a function that adds attributes to an object."""


def add_attribute(obj, att, value):
    """Add new attribute to an object if possible.

    Args:
        obj (any): The object to add an attribute to it.
        att (str): The name of the attribute.
        value (any): The value of attribute.
    Raises:
        TypeError: If the attribute cannot be added to obj.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
