#!/usr/bin/python3

"""100-my_int
Defines class My_int.
"""


class My_int:
    """
    Inherits from built-in int.

    methods
    -------
    __new__
        x
    __eq__
        x
    __ne__
        x
    """

    def __new__(cls, value):
        """x"""

        return super(MyInt, cls).__new__(cls, value)

    def __eq__(self, other):
        """x"""

        return not super(MyInt, self).__eq__(other)

    def __ne__(self, other):
        """x"""

        return not super(MyInt, self).__ne__(other)
