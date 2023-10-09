#!/usr/bin/python3
"""Module to define a class"""
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
        - x (int, optional): The x-coordinate of the square's position.
        - y (int, optional): The y-coordinate of the square's position.
        - id: An optional identifier for the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the current size of the square."""
        self.width = value
        self.height = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
