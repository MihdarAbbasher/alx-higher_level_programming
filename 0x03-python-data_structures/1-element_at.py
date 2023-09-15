#!/usr/bin/python3
def element_at(my_list, idx):
    """get element at index"""
    list_len = len(my_list)
    if idx >= list_len or idx < 0:
        return None

    return my_list[idx]
