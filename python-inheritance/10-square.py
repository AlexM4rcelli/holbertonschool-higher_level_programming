#!/usr/bin/python3
"""Define a class Square."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a Square object.

        Args:
            size (int): The size of the square's sides.

        Attributes:
            __size (int): The size of the square's sides.
        """ 
        super().__init__(size, size)
        self.__size = size
    
    def area(self):
        """Initialize a Square object.

        Args:
            size (int): The size of the square's sides.

        Attributes:
            __size (int): The size of the square's sides.
        """ 
        return self.__size * self.__size
