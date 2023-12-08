#!/usr/bin/python3

"""10-square
Defines class Square.
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Inherits from Rectangle

    methods
    -------
    area()
        Calculates area of a square.
    """

    def __init__(self, size):
        """validates values"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """return the area of current square"""

        return self.__size ** 2
