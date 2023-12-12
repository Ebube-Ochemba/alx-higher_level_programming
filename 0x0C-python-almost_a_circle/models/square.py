#!/usr/bin/python3

"""
square
Defines a class Square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherit from Rectangle and set size as width and height.

    methods
    -------
    __str__()
        return [Square] (<id>) <x>/<y> - <size>
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        parameters
        ----------
        size (int): The size of the square.
        x (int): ...
        y (int): ...
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return [Square] (<id>) <x>/<y> - <size>"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
