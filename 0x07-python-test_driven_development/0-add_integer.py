#!/usr/bin/python3

"""
0-add_integer
Contains a function that add two integers.
"""


def add_integer(a, b=98):
    """Computes and returns the sum of two integers.

    Args:
        a (int or float): The first value.
        b (int or float): The second value.

    Return:
        An int representing the sum of 'a' and 'b'.

    Raises:
        TypeError: An error occurs when 'a' or 'b' is not an int or float.
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
