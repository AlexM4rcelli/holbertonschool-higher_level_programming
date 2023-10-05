#!/usr/bin/python3
"""Check if instance of a class that inherited (directly or indirectly)
from the specified class"""


def inherits_from(obj, a_class):
    """
        Args:
            @obj: Object to check if is instance of the other one
            @a_class: Object to check if is a super class of obj
        Return:
            True if the object is exactly an instance of the specified class,
            otherwise False
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
