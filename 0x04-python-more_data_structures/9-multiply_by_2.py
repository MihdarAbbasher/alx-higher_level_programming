#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """returns a new dictionary with double values"""
    new_dic = {key: (a_dictionary[key] * 2) for key in a_dictionary}
    return new_dic
