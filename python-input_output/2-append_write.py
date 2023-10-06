#!/usr/bin/python3
"""Module to a function"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file (UTF8) and returns the number
    of characters added
    """
    with open(filename, 'a', encoding="utf-8") as file:
        char_count = file.write(text)
    return char_count
