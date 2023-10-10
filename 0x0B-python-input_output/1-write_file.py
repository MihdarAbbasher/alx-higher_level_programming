#!/usr/bin/python3

"""Defines a def read file."""


def write_file(filename="", text=""):
    """write txt to file filename"""
    with open(filename, mode='w', encoding='utf-8') as myFile:
        myFile.write(text)
