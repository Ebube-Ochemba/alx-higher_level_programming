#!/usr/bin/python3

"""9-student
Defines a class student.
"""


class Student:
    """
    Defines a Student
    ...

    Attributes
    ----------
    first_name : string
        undefined
    last_name : string
        undefined
    age : string
        undefined

    methods
    -------
    to_json()
        Returns dictionary description of an object.
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns dictionary description with simple data structure for JSON
        serialization of an object.
        """

        return self.__dict__
