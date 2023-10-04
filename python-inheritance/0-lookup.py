#!/usr/bin/python3
"""
Function that returns the list of available attributes and
methods of an object
"""


def lookup(obj):
    """
    Args:
        @obj: object to return their attributes and methods
    Return:
        list of available attributes and methods
    """
    return list(dir(obj))
