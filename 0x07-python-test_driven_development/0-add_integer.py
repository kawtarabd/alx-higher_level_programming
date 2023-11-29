#!/usr/bin/python3
"""function that adds two integer."""


def add_integer(a, b=98):
    """adds_integers.

    :parametre a: number.
    :parametre b: number.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
