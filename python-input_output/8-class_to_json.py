#!/usr/bin/python3
"""Module to a function"""


def class_to_json(obj):
    """
    returns the dictionary description with simple data structure for
    JSON serialization of an object
    """

    serialized_obj = {}
    for attr in dir(obj):
        if not attr.startswith('__'):
            if isinstance(getattr(obj, attr), (int, str, bool, list, dict)):
                serialized_obj[f"{attr}"] = getattr(obj, attr)
    return serialized_obj
