#!/usr/bin/python3
def max_integer(my_list=[]):
    len1 = len(my_list)
    if len1 == 0:
        return (None)

    biggest = my_list[0]
    for i in range(len1):
        if my_list[i] > biggest:
            biggest = my_list[i]
    return (biggest)
