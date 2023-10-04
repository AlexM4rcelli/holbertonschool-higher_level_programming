#!/usr/bin/python3
"""Module to a function that compare two objects"""


def is_same_class(obj, a_class):
    """ 
        Args:
            @obj: Object to check if is instance of the other one
            @a_class: Object to check if is a super class of obj
        Return:
            True if the object is exactly an instance of the specified class,
            otherwise False
    """
    return type(obj) is a_class
