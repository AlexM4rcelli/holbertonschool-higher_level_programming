#!/usr/bin/python3
"""Module to a function"""
import json


def to_json_string(my_obj):
    """parse the Python object and convert it to a JSON string"""
    return json.dumps(my_obj)
