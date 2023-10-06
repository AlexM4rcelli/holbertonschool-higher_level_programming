#!/usr/bin/python3
"""Module to a function"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8) and returns the number
    of characters written
    """
    with open(filename, 'w', encoding="utf-8") as file:
        char_count = file.write(text)
    return char_count
