#!/usr/bin/python3

"""
8-class_to_json

"""


def class_to_json(obj):

    """Returns dictionary description with simple data structure for JSON
    serialization of an object.
    """

    return obj.__dict__
