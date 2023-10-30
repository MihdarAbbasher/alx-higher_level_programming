#!/usr/bin/python3
"""Module defines lookup method."""

class MyList(list):
    """list class inherits from list"""
    def print_sorted(self):
        """print list in ascending order"""
        print(sorted(self))
