#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    list division.

    Args:
    my_list_1 - list 1
    my_list_2 - list 2
    list_length - len

    Return:
    count
    """

    li = []
    for i in range(list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
            li.append(res)
        except (ZeroDivisionError, TypeError, IndexError) as e:
            if isinstance(e, TypeError):
                print("wrong type")
            elif (isinstance(e, ZeroDivisionError)):
                print("division by 0")
            elif (isinstance(e, IndexError)):
                print("out of range")
            li.append(0)
        finally:
            pass

    return li
