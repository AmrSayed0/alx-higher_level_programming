#!/usr/bin/python3

from print_square import print_square

# Call print_square with various values of size
print_square(4)
print("")
print_square(10)
print("")
print_square(0)
print("")
print_square(1)
print("")

# Call print_square with invalid values of size
try:
    print_square(-1)
except Exception as e:
    print(e)
