#!/usr/bin/python3

"""
9-Rectangle
Defines class Rectangle
"""


class Rectangle:
    """
    Defines a Rectangle
    ...

    Attributes
    ---------
    number_of_instances : int
        Increments/decrements per instance instantiation/deletion.
    print_symbol : any
        Used as symbol for string representation.
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
    bigger_or_equal(rect_1, rect_2)
        Find the biggest rectangle based on the area.
    square
        A class method that returns a new Rectangle instance.
    """

    number_of_instances = 0
    print_symbol = '#'

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
                    rec = rec + str(self.print_symbol)
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Find the biggest rectangle based on the area.

        parameters
        ----------
        rect_1 : Rectangle
            An instance of Rectangle to compare.
        rect_2 : Rectangle
            An instance of Rectangle to compare.

        Raise
        -----
        TypeError
            If rect_1 or rect_2 is not an instance of Rectangle

        return: the biggest rectangle.
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_rect_1 = rect_1.__width * rect_1.__height
        area_rect_2 = rect_2.__width * rect_2.__height

        if area_rect_1 >= area_rect_2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        A class method that returns a new Rectangle instance.

        return: a new Rectangle instance with width == height == size
        """

        return cls(size, size)
