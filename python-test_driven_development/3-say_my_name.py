#!/usr/bin/python3
"""This module prints the name of a anything"""


if __name__ == "__main__":
    def say_my_name(first_name, last_name=""):
        """
        Print a message with the given first name and last name.

        Args:
            first_name (str): The first name.
            last_name (str, optional): The last name (def: an empty string).

        Raises:
            TypeError: If first_name or last_name is not a string.
        """

        if not isinstance(first_name, str):
            raise TypeError("first_name must be a string")

        if not isinstance(last_name, str):
            raise TypeError("last_name must be a string")

        print("My name is {} {}".format(first_name, last_name))
