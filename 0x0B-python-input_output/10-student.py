#!/usr/bin/python3

"""10-student
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

    def to_json(self, attrs=None):
        """Returns dictionary description with simple data structure for JSON
        serialization of an object.
        """

        rep_dic = self.__dict__

        if type(attrs) is list:
            rep_dic = {key: value for key, value in rep_dic.items()
                       if key in attrs}

        return rep_dic
