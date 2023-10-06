#!/usr/bin/python3
"""Module Squire that contain empty class.

this is a square class with attr.
"""


class Square:
    """empty square proto type."""

    def __init__(self, size=0):
        """initialize instance with size
            Args:
                size: size of square
        """

        if (isinstance(size, int)):
            if (size < 0):
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return self.__size * self.__size
