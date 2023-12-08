#!/usr/bin/python3

"""8-rectangle
Defines class Rectangle.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Inherits from BaseGeometry.
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
