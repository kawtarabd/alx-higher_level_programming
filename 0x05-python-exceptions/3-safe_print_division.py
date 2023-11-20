#!/usr/bin/python3

def safe_print_division(a, b):
    rslt = 0
    try:
        rslt = a / b
    except ZeroDivisionError:
        rslt = None
    finally:
        print("Inside result: {}".format(rslt))
    return rslt
