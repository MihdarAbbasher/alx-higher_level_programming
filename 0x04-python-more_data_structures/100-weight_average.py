#!/usr/bin/python3
def weight_average(my_list=[]):
    """Returns the weighted average of all integers tuple(s, w)"""
    if not my_list:
        return 0

    score_sum = 0
    weight_sum = 0

    for tuple_pair in my_list:
        score_sum += tuple_pair[0] * tuple_pair[1]
        weight_sum += tuple_pair[1]

    return (score_sum / weight_sum)
