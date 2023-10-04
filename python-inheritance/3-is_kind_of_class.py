#!/usr/bin/python3
"""
Module for a function that is an instance of, or if the object
is an instance of a class that inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """
        Args:
            @obj: Object to check if is instance of the other one
            @a_class: Object to check if is a super class of obj
        Return:
            True if the object is exactly an instance of the specified class,
            otherwise False
    """
    return isinstance(obj, a_class)
