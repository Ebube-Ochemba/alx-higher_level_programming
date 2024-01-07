#!/usr/bin/python3

"""100-my_int
Defines class MyInt.
"""


class MyInt(int):
    """
    Inherits from built-in int.

    methods
    -------
    __eq__
        Inverts __eq__ result.
    __ne__
        Inverts __ne__ result.
    """

    def __eq__(self, other):
        """Inverts __eq__ result"""

        return False

    def __ne__(self, other):
        """Inverts __ne__ result"""

        return True
