#!/usr/bin/python3

"""Defines a function for class checking."""


def is_same_class(obj, a_class):
    """Check if an object is an instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to check with.
    Returns:
        If obj is an instance of a_class => True.
        Otherwise => False.
    """
    if type(obj) == a_class:
        return True
    return False
