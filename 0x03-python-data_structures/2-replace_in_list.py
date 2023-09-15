#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """replace list item at index"""
    list_len = len(my_list)
    if idx >= list_len or idx < 0:
        return my_list
    my_list[idx] = element
    return my_list
