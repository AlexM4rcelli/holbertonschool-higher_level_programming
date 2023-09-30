#!/usr/bin/python3

def max_integer(list=[]):
    """
    Find and return the maximum integer in a list of integers.

    Args:
        lst (list): The list of integers.

    Returns:
        int: The maximum integer in the list
        None: If the list is empty.
    """

    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
