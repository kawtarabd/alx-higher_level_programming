#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0
    rslt = 0
    div = 0
    for k in my_list:
        rslt += k[0] * k[1]
        div += k[1]
    rslt /= div
    return rslt
