#!/usr/bin/python3

"""0-lookup
This module returns the list of available attributes and methods
of an object.
"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object
    """

    get = dir(obj)
    return get
