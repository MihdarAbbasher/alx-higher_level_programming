#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """deletes a key in a dictionary if it exists."""
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
