#!/usr/bin/python3

"""11-square
Defines a class Square.
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Inherits from Rectangle

    methods
    -------
    area()
        Calculates area of a square.
    __str__
        Returns the square description.
    """

    def __init__(self, size):
        """Validates values"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of current square"""

        return self.__size ** 2

    def __str__(self):
        """Returns the square description:
        [Square] <width>/<height>
        """

        return "[Square] {}/{}".format(self.__size, self.__size)
