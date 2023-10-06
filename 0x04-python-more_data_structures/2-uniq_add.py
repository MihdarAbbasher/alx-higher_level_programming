#!/usr/bin/python3
def uniq_add(my_list=[]):
    """add once every element in a list"""
    if not my_list:
        return 0

    res = 0
    unique_set = set(my_list)
    for x in unique_set:
        res += x
    return res
