#!/usr/bin/python3

"""Defines a function to check inherited class checking."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to check the type of obj with.
    Returns:
        If obj is an inherited instance of a_class => True.
        Otherwise => False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
