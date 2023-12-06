#!/usr/bin/python3

"""
2-write_file
Appends a string at the end of a text file.
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file, create if it doesn't exit.

    return: The number of characters written.
    """
    with open(filename, 'a', encoding=("utf8")) as file:
        written = file.write(text)
        return written
