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
    @property
    def size(self):
        """get size of square.
        Return:
            size.
        """
        return self.__size
    @size.setter
    def size(self, v):
        """set size of square.
        Args:
            v: new value of size
        """
        if (isinstance(v, int)):
            if (v < 0):
                raise ValueError("size must be >= 0")
            self.__size = v
        else:
            raise TypeError("size must be an integer")

    def my_print(self):
        """print square with char '#'."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
