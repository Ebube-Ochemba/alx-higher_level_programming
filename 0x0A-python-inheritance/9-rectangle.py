#!/usr/bin/python3

"""9-rectangle
Defines a class Rectangle.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Inherits from BaseGeometry.

    methods
    -------
    area()
        Calculates area of a Rectangle.
    __str__
        return a descrpition.
    """

    def __init__(self, width, height):
        """
        Parameters
        ----------
        width : int
            The width of the rectangle.
        height : int
            The height of the rectangle.
        """

        super().integer_validator("width", width)
        self.__width = width

        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calculates the area of the current Rectangle

        return: The area of current Rectangle.
        """

        return (self.__width * self.__height)

    def __str__(self):
        """return a descrpition"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
