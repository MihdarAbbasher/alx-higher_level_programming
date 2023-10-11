#!/usr/bin/python3
"""Module defines lookup method."""


def lookup(obj):
    """returns list of available attributes and methods of obj"""

    return (dir(obj))
