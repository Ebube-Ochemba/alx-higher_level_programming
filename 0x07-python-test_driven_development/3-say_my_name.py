#!/usr/bin/python3

"""
3-say_my_name
prints My name is <first name> <last name>.
"""


def say_my_name(first_name, last_name=""):
    """x
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
