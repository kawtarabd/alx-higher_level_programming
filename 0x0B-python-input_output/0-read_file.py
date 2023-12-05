#!/usr/bin/python3
"""the function"""


def read_file(filename=""):
    """read_file.

    :param filename:
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
