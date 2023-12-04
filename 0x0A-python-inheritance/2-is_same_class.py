#!/usr/bin/python3

"""2-is_same_class
Defines a function is_same_class()
"""


def is_same_class(obj, a_class):
    """Checks if the object is exactly an instance of the specified class.
    return: True if it is an exact instance, else False.
    """

    return type(obj) is a_class
