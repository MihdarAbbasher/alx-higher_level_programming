#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """print list items in reverse"""
    lenn = len(my_list)
    for i in range(lenn - 1, -1, -1):
        print("{:d}".format(my_list[i]))
