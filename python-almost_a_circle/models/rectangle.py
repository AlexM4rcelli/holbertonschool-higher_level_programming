#!/usr/bin/python3
"""Module to define a class"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class representing a rectangle with dimensions and position.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle's position.
        y (int): The y-coordinate of the rectangle's position.
        id (int): An optional unique identifier for the rectangle.

    Methods:
        area(self): Calculates and returns the area of the rectangle.
        display(self): Displays the rectangle using '#' characters.
        __str__(self): Returns a string representation of the rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle instance.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.y = y
        self.x = x

    @property
    def x(self):
        """Get/set the current x of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the current x of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get/set the current y of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the current y of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @property
    def width(self):
        """Get/set the current width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the current width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the current height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the current height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Display the rectangle using '#' characters.

        If the width or height is 0, it will print an empty line.
        """
        if self.__width == 0 or self.__height == 0:
            print()
        else:
            for _ in range(self.__y):
                print()
            for _ in range(self.__height):
                print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        Returns:
            str: string representation of the rectangle.
        """
        return (
            f"[{type(self).__name__}] ({self.id}) {self.__x}/{self.__y} -"
            f" {self.__width}/{self.__height}"
        )

    def update(self, *args):
        """
        Update the attributes of the rectangle.

        The arguments should be provided in the following order:
        1st argument: id attribute
        2nd argument: width attribute
        3rd argument: height attribute
        4th argument: x attribute
        5th argument: y attribute
        """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]

