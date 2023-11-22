#!/usr/bin/python3

"""
6-square
Defines class Square
"""


class Square:
    """
    Defines a Square
    ...

    Attributes
    ----------
    size : int
        The size of a side of the square
    position : tuple
        A tuple of 2 positive integers

    methods
    -------
    area()
        Calculates the area of the current square.
    my_print()
        Prints the square in stdout with the character '#'.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Parameters
        ----------
        size : int
            The size of a side of the square
        position : tuple
            A tuple of 2 positive integers.

        Raise
        -----
        TypeError
            If size is not an integer.
        ValueError
            If "size must be < 0.
        """

        self.__size = size

    @property
    def size(self):
        """
        getter

        returns: The squares size.
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter

        Parameters
        ----------
        value : int
            The size of a side of the square

        Raise
        -----
        TypeError
            If size is not an integer.
        ValueError
            If size is < 0.
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        getter

        returns: A tuple of 2 positive integers.
        """

        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter

        Parameters
        ----------
        value : tuple
             A tuple of 2 positive integers.

        Raise
        -----
        TypeError
            If po
        """

        x

    def area(self):
        """
        Calculates the area of the current square

        return: The area of current square.
        """

        return self.__size ** 2

    def my_print(self):
        """
        Prints the square in stdout with the character '#'

        return: None.
        """
        if self.__size == 0:
            print("")
        else:
            for obi in range(self.__size):
                for obj in range(self.__size):
                    print("#", end='')
                print("")
