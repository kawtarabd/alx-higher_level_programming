#!/usr/bin/python3
"""Rectangle."""


class Rectangle:
    """Representation of Rectangle."""
    def __init__(self, width=0, height=0):
        """Initialisation the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """width.

        :param value: the value.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """height.

        :param value: the value.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area."""
        return self.__height * self.__width

    def perimeter(self):
        """returns the perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
