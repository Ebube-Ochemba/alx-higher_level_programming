#!/usr/bin/python3

"""
5-save_to_json_file
"""


import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file, using json representation"""

    with open(filename, 'w', encoding="utf8") as file:
        json.dump(my_obj, file)
