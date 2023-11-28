#!/usr/bin/python3

"""
100-locked_class
Defines a locked class
"""

class LockedClass:
    """
    A locket class that prevents dynamic creation a new instance attribute,
    except if the new instance attribute is called "first_name"
    """

    __slots__ = ["first_name"]
