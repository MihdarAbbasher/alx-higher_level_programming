#!/usr/bin/python3
def roman_to_int(roman_string):
    """ converts a Roman num to an integer."""
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if (roman_string is None) or (type(roman_string) is not str):
        return 0

    lenn = len(roman_string)
    int_value = dic[roman_string[lenn - 1]]
    for i in range(lenn - 1, 0, -1):
        current_value = dic[roman_string[i]]
        next_value = dic[roman_string[i - 1]]

        if current_value <= next_value:
            int_value += next_value
        else:
            int_value -= next_value

    return int_value
