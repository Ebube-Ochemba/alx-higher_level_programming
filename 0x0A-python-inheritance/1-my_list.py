#!/usr/bin/python3

"""1-my_list.py
This module defines a class 'Mylist'.
"""


class MyList(list):
    """Inherits from a class 'list', it is a subclass of 'list'.
    """

    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """Prints the list sorted in ascending order.
        """

        print(sorted(self))
