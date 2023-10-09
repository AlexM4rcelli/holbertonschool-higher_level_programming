#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class representing a square, which is a special case of a rectangle.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square object.

        Args:
        - size (int): The size of the square's sides.
        - x (int, optional): The x-coordinate of the square's position (default is 0).
        - y (int, optional): The y-coordinate of the square's position (default is 0).
        - id: An optional identifier for the square.
        """
        super().__init__(size, size, x, y)
