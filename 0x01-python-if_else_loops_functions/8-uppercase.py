#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if (ord(str[i]) >= 97) and (ord(str[i]) <= 122):
            ascVal = 32
        else:
            ascVal = 0
        print("{}".format(chr(ord(str[i]) - ascVal)), end="")
    print()
