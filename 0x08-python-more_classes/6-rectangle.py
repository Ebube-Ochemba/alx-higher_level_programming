#!/usr/bin/python3

"""
6-Rectangle
Defines class Rectangle
"""


class Rectangle:
    """
    Defines a Rectangle
    ...

    Attributes
    ---------
    number_of_instances : int
    increments/decrements per instance instantiation/deletion.
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
    __str__
        Builds a string of '#' that representa a rectangle.
    __repr__
        Builds a string representation of code to recreate a new instance.
    __del__
        Print the a message when an instance of rectangle is deleted.
    """

    number_of_instances = 0

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
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """
        Builds a string of '#' that representa a rectangle.

        return: A string of '#' that represents a rectangle.
        """

        if self.__width == 0 or self.__height == 0:
            return ("")
        else:
            rec = ""
            for row in range(self.__height):
                for column in range(self.__width):
                    rec = rec + "#"
                if row != self.__height - 1:
                    rec = rec + "\n"
        return rec

    def __repr__(self):
        """
        Builds a string representation of code to recreate a new instance.

        return: string representation of code to rebuild the rectangle.
        """

        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        """
        Print the message "Bye rectangle..."  when an instance of Rectangle
        is deleted.

        return: None.
        """

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
