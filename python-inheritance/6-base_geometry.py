#!/usr/bin/python3
"""Define a class BaseGeometry."""


class BaseGeometry:
    """Represent a geometry base."""

    def area(self):
        """Calculate the area of the geometric shape.

        Raises:
            Exception: This method should be implemented in subclasses.
        """
        raise Exception("area() is not implemented")
