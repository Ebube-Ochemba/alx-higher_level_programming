#!/usr/bin/python3

"""
1-write_file
writes a string to a text file.
"""


def write_file(filename="", text=""):
    """Writes into file, create if it doesn't exit

    return: The number of characters written.
    """

    with open(filename, 'w', encoding=("utf8")) as file:
        written = file.write(text)
        return written
