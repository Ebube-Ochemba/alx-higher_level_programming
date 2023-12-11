#!/usr/bin/python3

"""
base
Defines a class Base.
"""


class Base:
    """
    Defines a class Base
    ...

    Attributes
    ----------
    __nb_objects (int):

    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        parameters
        ----------
        id (int): update...
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
