#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle:
    """Represent a Rectangle."""
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get/set the current width of the square."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the square."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the current height of the square."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the square."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
