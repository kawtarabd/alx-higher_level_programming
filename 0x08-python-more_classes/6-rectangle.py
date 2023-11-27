#!/usr/bin/python3
"""Definition Rectangle."""


class Rectangle:
    """Representation Rectangle."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """__init__.

        :param width: width of the Rectangle.
        :param height: height of the Rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """returns width."""
        return self.__width

    @width.setter
    def width(self, value):
        """returns width.

        :param value: the value.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns height."""
        return self.__height

    @height.setter
    def height(self, value):
        """returns height.

        :param value: the value.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area."""
        return self.__height * self.__width

    def perimeter(self):
        """perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """__str__."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join(['#' * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """__repr__."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """__del__."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
