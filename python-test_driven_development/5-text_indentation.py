#!/usr/bin/python3
"""
This module prints a text with a 2 new lines after each of
these characters: `.`, `?`, `:`
"""


def text_indentation(text):
    """
    Print a text with 2 new lines after each '.', '?', and ':' character.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = []
    for char in text:
        if char in ".?:":
            result.append(char + "\n\n")
        else:
            result.append(char)

    formatted_text = "".join(result)
    print(formatted_text)
