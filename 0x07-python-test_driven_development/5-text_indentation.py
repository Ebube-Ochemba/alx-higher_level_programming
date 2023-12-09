#!/usr/bin/python3

"""
5-text_indentation
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of
    these characters: '.', '?' and ':'.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in text:
        if char in [".", "?", ":"]:
            print(char, end='\n\n')
        else:
            print(char, end='')
