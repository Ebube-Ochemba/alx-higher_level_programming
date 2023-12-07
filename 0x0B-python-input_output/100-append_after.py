#!/usr/bin/python3

"""
100-append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line containing
    a specific string.
    """

    with open(filename, 'r') as file:
        lines = file.readlines()

    for i in range(len(lines)):
        if search_string in lines[i]:
            lines[i] += new_string

    with open(filename, 'w') as file:
        file.writelines(lines)
