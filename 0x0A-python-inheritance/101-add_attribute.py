#!/usr/bin/python3
"""
101-adds_atribute
A function that adds a new attribute to an object if it’s possible.
"""


def add_attribute(obj, attr, value):
    """A function that adds a new attribute to an object,
    if it’s possible.
    """

    if hasattr(obj, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
