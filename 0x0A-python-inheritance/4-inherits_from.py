#!/usr/bin/python3

"""4-inherits_from
Defines a function inherits_from().
"""


def inherits_from(obj, a_class):
    """Checks if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    return: True if the object is an instance of a class that inherited
    from the specified class, else False.
    """

    return issubclass(type(obj), a_class) and type(obj) is not a_class
