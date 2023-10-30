#!/usr/bin/python3

"""Defines a function that check class and inherited class obj."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to check the type of obj with.
    Returns:
        If obj is an instance or inherited instance of a_class => True.
        Otherwise => False.
    """
    if isinstance(obj, a_class):
        return True
    return False
