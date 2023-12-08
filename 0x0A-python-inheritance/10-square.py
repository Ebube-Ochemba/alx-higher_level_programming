#!/usr/bin/python3

"""10-square
Defines a class Square.
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
        """Validates values"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of current square"""

        return self.__size ** 2
