#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class CustomRectangle(Base):
    """Represent a rectangle."""

    def __init__(self, w, h, x=0, y=0, identity=None):
        """Initialize a new CustomRectangle.

        Args:
            w (int): The width of the new CustomRectangle.
            h (int): The height of the new CustomRectangle.
            x (int): The x coordinate of the new CustomRectangle.
            y (int): The y coordinate of the new CustomRectangle.
            identity (int): The identity of the new CustomRectangle.
        Raises:
            TypeError: If either of w or h is not an int.
            ValueError: If either of w or h <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        super().__init__(identity)

    @property
    def w(self):
        """Set/get the width of the CustomRectangle."""
        return self.__w

    @w.setter
    def w(self, value):
        if type(value) != int:
            raise TypeError("w must be an integer")
        if value <= 0:
            raise ValueError("w must be > 0")
        self.__w = value

    @property
    def h(self):
        """Set/get the height of the CustomRectangle."""
        return self.__h

    @h.setter
    def h(self, value):
        if type(value) != int:
            raise TypeError("h must be an integer")
        if value <= 0:
            raise ValueError("h must be > 0")
        self.__h = value

    @property
    def x(self):
        """Set/get the x coordinate of the CustomRectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set/get the y coordinate of the CustomRectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the CustomRectangle."""
        return self.w * self.h

    def display(self):
        """Print the CustomRectangle using the `#` character."""
        if self.w == 0 or self.h == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.h):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.w)]
            print("")

    def update(self, *args, **kwargs):
        """Update the CustomRectangle.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents identity attribute
                - 2nd argument represents w attribute
                - 3rd argument represent h attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args:
            if len(args) > 5:
                raise TypeError("update() takes at most 5 positional arguments")
            attributes = ['id', 'w', 'h', 'x', 'y']
            for index, value in enumerate(args):
                setattr(self, attributes[index], value)
        else:
            for key, value in kwargs.items():
                if key in ['id', 'w', 'h', 'x', 'y']:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the CustomRectangle."""
        return {
        'id': self.id,
        'width': self.w,
        'height': self.h,
        'x': self.x,
        'y': self.y,
    }
