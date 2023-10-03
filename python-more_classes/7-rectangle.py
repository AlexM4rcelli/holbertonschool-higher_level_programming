#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle:
    """Represent a Rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle."""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get/set the current width of the square."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the square."""
        self.__width = value

    @property
    def height(self):
        """Get/set the current height of the square."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the square."""
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """"Returns the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        result = ""
        for i in range(self.__height):
            for j in range(self.__width):
                result += str(self.print_symbol)
            if i != self.__height - 1:
                result += '\n'
        return result

    def __repr__(self):
        return "Rectangle({},{})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
        del self
