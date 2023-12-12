#!/usr/bin/python3

"""
rectangle
Defines a class Rectangle
"""


from models.base import Base


class Rectangle(Base):
    """
    Defines a Rectangle
    ...

    Attributes
    ----------
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.
    x (int): ...
    y (int): ...

    methods
    -------
    area()
        Calculates the area of the current Rectangle.
    display()
        Prints in stdout the Rectangle instance with the character #.
    __str__()
        Returns [Rectangle] (<id>) <x>/<y> - <width>/<height>.
    update()
        Updates the rectangle's attributes.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Parameters
        ----------
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): ...
        y (int): ...
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter

        Parameters
        ----------
        width (int): The width of a  Rectangle.

        Raise
        -----
        TypeError: If width is not an integer.
        ValueError: If width is <= 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter

        Parameters
        ----------
        height (int): The height of a  Rectangle.

        Raise
        -----
        TypeError: If height is not an integer.
        ValueError: If height is <= 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter

        Parameters
        ----------
        x (int): ...

        Raise
        -----
        TypeError: If x is not an integer.
        ValueError: If x is < 0.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter

        Parameters
        ----------
        y (int): ...

        Raise
        -----
        TypeError: If y is not an integer.
        ValueError: If y is < 0.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates the area of the current Rectangle

        return: The area of current Rectangle.
        """
        return (self.width * self.height)

    def display(self):
        """Prints the rectangle to stdout"""
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return (
                f"[Rectangle] ({self.id}) "
                f"{self.x}/{self.y} - "
                f"{self.width}/{self.height}"
            )

    def update(self, *args, **kwargs):
        """Update the rectangle's attributes"""
        if args:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        if kwargs:
            for key, value in kwargs.items():
                if key in ['id', 'width', 'height', 'x', 'y']:
                    setattr(self, key, value)
