#!/usr/bin/python3
"""Check if instance of a class that inherited (directly or indirectly)
from the specified class"""


def inherits_from(obj, a_class):
    """check if its a subclass or not"""
    return isinstance(obj, a_class) and type(obj) is not a_class
