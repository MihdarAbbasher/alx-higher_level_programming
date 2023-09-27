#!/usr/bin/python3

def safe_print_division(a, b):
    """ safe_print_ division.

    Args:
    a
    b

    Return:
    result
    """

    try:
        res = a / b
    except (ZeroDivisionError):
        res = None
    finally:
        print("Inside result: {}".format(res))
    return (res)
