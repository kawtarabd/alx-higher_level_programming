#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    listdivs = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            listdivs.append(True)
        else:
            listdivs.append(False)
    return listdivs
