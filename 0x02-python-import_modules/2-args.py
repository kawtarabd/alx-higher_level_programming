#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    counter = len(sys.argv) - 1
    if counter == 0:
        print("0 arguments.")
    else:
        if counter == 1:
            print("{} argument:".format(counter))
        else:
            print("{} arguments:".format(counter))
        for i in range(1, counter + 1):
            print("{}: {}".format(i, sys.argv[i]))
