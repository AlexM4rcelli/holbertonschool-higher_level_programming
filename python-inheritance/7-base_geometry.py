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

    def integer_validator(self, name, value):
        """Validate if a value is a positive integer.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError("{:} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:} must be greater than 0".format(name))
