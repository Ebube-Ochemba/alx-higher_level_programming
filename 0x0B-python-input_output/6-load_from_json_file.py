#!/usr/bin/python3

"""
6-load_from_json_file
"""


import json


def load_from_json_file(filename):
    """creates and object from a JSON file"""

    with open(filename, 'r', encoding="utf8") as file:
        new = json.load(file)
    return new
