#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """replace list item at index"""
    list_len = len(my_list)
    new_list = []
    for i in range(list_len):
        if i == idx:
            new_list.append(element)
        else:
            new_list.append(my_list[i])

    return new_list
