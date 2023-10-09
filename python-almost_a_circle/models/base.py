#!/usr/bin/python3
"""Module to define a class"""
import json


class Base:
    """
    This class provides a mechanism for assigning unique IDs to objects.
    It keeps track of the number of objects created and assigns each
    object a unique ID starting from 1.

    Attributes:
        __nb_objects (int): A class attribute to keep track of the number
        of objects created.
        id (int): An instance attribute representing the unique ID assigned
        to an object.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if isinstance(id, int):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries:
            return "[]"

        return str(json.dumps(list_dictionaries))
