#!/usr/bin/python3

"""
3-square
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
    def __init__(self, size=0):
        """
        Parameters
        ----------
        size : int
            The size of a side of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    
    def area(self):
