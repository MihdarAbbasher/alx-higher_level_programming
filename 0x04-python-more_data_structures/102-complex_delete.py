#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """Deletes keys with a specific value in a dictionary."""

    keys = list(a_dictionary.keys())
    for k in keys:
        if value == a_dictionary[k]:
            del a_dictionary[k]

    return (a_dictionary)
