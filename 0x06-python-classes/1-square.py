#!/usr/bin/python3

"""
1-square
Defines class Square with private attribute size
"""


class Square:
    """
    Defines a Square
    ...

    Attributes
    ----------
    size : int
        The size of a side of the square
    """
    def __init__(self, size):
        """
        Parameters
        ----------
        size : int
            The size of a side of the square
        """
        self.__size = size
