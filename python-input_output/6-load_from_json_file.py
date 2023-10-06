#!/usr/bin/python3
"""Module to a function"""
import json


def load_from_json_file(filename):
    """
        parse the JSON content from the file and convert
        to a Python Object
    """
    with open(filename, 'r') as file:
        return json.load(file)
