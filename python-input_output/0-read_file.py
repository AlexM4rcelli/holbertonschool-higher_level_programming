#!/usr/bin/python3
"""Module to a function"""

def read_file(filename=""):
    """
    eads a text file (UTF8) and prints it to stdout
    """
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end="")
