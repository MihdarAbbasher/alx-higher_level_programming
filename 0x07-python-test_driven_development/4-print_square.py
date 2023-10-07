#!/usr/bin/python3
"""Module contains a function that prints a square"""


def print_square(size):
    """ print square
        Arguments:
            @size: square size
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    if size == 0:
        return
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
