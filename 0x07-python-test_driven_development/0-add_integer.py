#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Returns the addition of two integers.

    Args:
        a (int): The first integer to be added.
        b (int, optional): The second integer to be added. Defaults to 98.

    Raises:
        TypeError: If either a or b is not an integer or a float.

    Returns:
        int: The addition of a and b.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
