#!/usr/bin/python3

"""
0-read_file
Reads a text file.
"""


def read_file(filename=""):
    """read a text file(utf9) and prints it to stdout"""

    with open(filename, "r", encoding=("utf8")) as text:
        lines = text.read()
    print(lines, end='')
