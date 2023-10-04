#!/usr/bin/python3
"""Defines a class that is a list"""


class MyList(list):
    """List Class"""


    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
