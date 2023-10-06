#!/usr/bin/python3
"""Module to a function"""
import json


def from_json_string(my_str):
    """parse the JSON string and convert it to a Python object"""
    return json.loads(my_str)
