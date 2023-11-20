#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    k = 0
    for item in my_list:
        try:
            if k < x:
                print("{}".format(item), end="")
                k += 1
        except IndexError:
            break
    print()
    return k
