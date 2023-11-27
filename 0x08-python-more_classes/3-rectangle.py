#!/usr/bin/python3

"""
3-Rectangle
Defines class Rectangle
"""


class Rectangle:
    """
    Defines a Rectangle
    ...

    Attributes
    ---------
    width : int
        The width of the rectangle.
    height : int
        The height of the rectangle.

    methods
    -------
    area()
        Calculates the area of the current Rectangle.
    perimeter()
        Calculates the perimeter of the current Rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Parameters
        ----------
        width : int
            The width of the rectangle.
        height : int
            The height of the rectangle.
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        getter

        returns: The Rectangles width.
        """

        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Setter

        Parameters
        ----------
        width : int
            The width of a  Rectangle.

        Raise
        -----
        TypeError
            If width is not an integer.
        ValueError
            If width is < 0.
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        getter

        returns: The Rectangles height.
        """

        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Setter

        Parameters
        ----------
        height : int
            The height of a  Rectangle.

        Raise
        -----
        TypeError
            If height is not an integer.
        ValueError
            If height is < 0.
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Calculates the area of the current Rectangle

        return: The area of current Rectangle.
        """

        return (self.__width * self.__height)

    def perimeter(self):
        """
        Calculates the perimeter of the current Rectangle

        return: The perimeter of current Rectangle.
        """

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))
