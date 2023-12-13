#!/usr/bin/python3

"""
base
Defines a class Base.
"""

import json


class Base:
    """
    Defines a class Base
    ...

    Attributes
    ----------
    __nb_objects (int): ...

    methods
    -------
    to_json_string
        Returns the JSON string representation of list_dictionaries.
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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
