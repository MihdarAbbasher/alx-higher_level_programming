#!/usr/bin/python3
"""Module defines lookup method."""

class MyList(list):
    """list class inherits from list"""
    def print_sorted(self):
        """returns list of available attributes and methods of obj"""
        print(sorted(self))
