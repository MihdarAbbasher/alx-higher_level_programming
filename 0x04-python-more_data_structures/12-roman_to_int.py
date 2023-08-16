#!/usr/bin/python3
def roman_to_int(roman_string):
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if (roman_string is None) or (type(roman_string) is not str):
        return 0

    lenn = len(roman_string)
    res = dic[roman_string[lenn - 1]]
    for i in range(lenn - 1, 0, -1):
        current_value = dic[roman_string[i]]
        previous_value = dic[roman_string[i - 1]]

        if previous_value >= current_value:
            res += previous_value
        else:
            res -= previous_value

    return res
