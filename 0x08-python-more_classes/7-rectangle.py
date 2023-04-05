#!/usr/bin/python3

class Rectangle:
    """A class that defines a rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a rectangle instance"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter method for the width of the rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the width of the rectangle"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter method for the height of the rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height of the rectangle"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle"""

        return self.width * self.height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle"""

        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return a string representation of the rectangle"""

        if self.width == 0 or self.height == 0:
            return ''
        return ((str(self.print_symbol) * self.width) + '\n') * self.height

    def __repr__(self):
        """Return a string representation of the rectangle"""

        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Delete the rectangle instance"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
