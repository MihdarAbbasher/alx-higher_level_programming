#!/usr/bin/python3

"""Defines a def read file."""


def read_file(filename=""):
    """read file filename"""
    with open(filename, encoding='utf-8') as myFile:
        txt = myFile.read()
        print(txt)
