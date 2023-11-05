#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None
    value = my_list[0]
    for i in range(1, len(my_list)):
        if value < my_list[i]:
            value = my_list[i]
    return value
