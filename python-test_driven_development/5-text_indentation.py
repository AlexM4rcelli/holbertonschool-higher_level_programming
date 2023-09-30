#!/usr/bin/python3

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

    sentences = []
    sentence = ""

    for char in text:
        if char in ['.', '?', ':']:
            sentences.append(sentence.strip())
            sentence = ""
        else:
            sentence += char

    if sentence:
        sentences.append(sentence.strip())

    for sentence in sentences:
        print(sentence)
        print("\n")
