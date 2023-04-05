#!/usr/bin/python3

def print_square(size):
    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    # Check if size is greater than or equal to 0
    if size < 0:
        raise ValueError("size must be >= 0")
    # Loop over the range of size
    for i in range(size):
        # Print a string of # characters of length size
        print("#" * size)
