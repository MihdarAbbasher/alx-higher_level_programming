#!/usr/bin/python3
"""Module defines lookup method."""

class MyList(list):
    """list class inherits from list"""
    def __init___(self):
        """init list"""
        super().__init__()
    def print_sorted(self):
        """returns list of available attributes and methods of obj"""
        print(sorted(self))
