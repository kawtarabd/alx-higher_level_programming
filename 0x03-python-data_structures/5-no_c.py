#!/usr/bin/python3

def no_c(my_string):
    ket = ""
    for char in my_string:
        if char != "c" and char != "C":
            ket += char
    return ket
