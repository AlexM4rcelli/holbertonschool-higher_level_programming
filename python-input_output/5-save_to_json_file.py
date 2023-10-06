#!/usr/bin/python3
"""Module to a function"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    with open(filename, 'w', encoding="utf-8") as file:
        char_count = file.write(json.dumps(my_obj))
