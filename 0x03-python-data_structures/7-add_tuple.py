#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """sum first two elements, assume 0 if not exist"""
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    new_t = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return new_t
