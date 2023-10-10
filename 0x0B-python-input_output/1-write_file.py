#!/usr/bin/python3

"""Defines a def read file."""


def write_file(filename="", text=""):
    """write txt to file filename
    Args:
        filename (str): The name of the file.
        text (str): The text to write to the file.
    Returns:
        The number of characters successfully written.

    """
    with open(filename, mode='w', encoding='utf-8') as myFile:
        return (myFile.write(text))
