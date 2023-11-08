#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal_val = 0
    prev_val = 0
    for numer in reversed(roman_string):
        val = dic[numer]
        if val >= prev_val:
            decimal_val += val
        else:
            decimal_val -= val
        prev_val = val
    return decimal_val
