#!/usr/bin/python3

"""7-base_geometry
Defines class BaseGeometry.
"""


class BaseGeometry:
    """Incomplete class

    methods
    -------
    area()
        An incomplete method.
    """

    def area(self):
        """An unimplemented public attribute.

        return: None.

        Raise
        -----
        Exception
            area() is not implemented
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks if 'value' is an int or is > 0.

        returm: None.

        Raise
        -----
        TypeError
            if 'name' is not an integer.
        ValueError
            if value <= 0.
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    1-Rectangle
    Defines class Rectangle
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

        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
