#!/usr/bin/python3
"""Module to a class"""


class Student:
    """Defines a Student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, args=None):
        "retrieves a dictionary representation of a Student instance"
        if type(args) is list and all(type(elem) is str for elem in args):
            return {k: getattr(self, k) for k in args if hasattr(self, k)}
        else:
            ser_obj = {}
            types = (int, str, bool, list, dict)
            for attr in dir(self):
                if not attr.startswith('__'):
                    if isinstance(getattr(self, attr), types):
                        ser_obj[f"{attr}"] = getattr(self, attr)
            return ser_obj

    def reload_from_json(self, json):
        """Replace all attributes of the Student."""
        for key, value in json.items():
            setattr(self, key, value)
