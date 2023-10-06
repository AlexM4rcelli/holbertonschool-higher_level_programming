#!/usr/bin/python3
"""Module to a class"""


class Student:
    """Defines a Student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a class"""
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

    def to_json(self):
        "retrieves a dictionary representation of a Student instance"
        serialized_obj = {}
        types = (int, str, bool, list, dict)
        for attr in dir(self):
            if not attr.startswith('__'):
                if isinstance(getattr(self, attr), types):
                    serialized_obj[f"{attr}"] = getattr(self, attr)
        return serialized_obj
