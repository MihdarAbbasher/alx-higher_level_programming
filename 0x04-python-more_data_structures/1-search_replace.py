#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """replaces element by another in new list"""
    if not my_list:
        return None

    newli = []
    for x in my_list:
        if x == search:
            newli.append(replace)
        else:
            newli.append(x)
    return newli
