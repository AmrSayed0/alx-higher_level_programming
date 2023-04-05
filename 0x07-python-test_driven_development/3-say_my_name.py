#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    # Check if first_name is a string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    # Check if last_name is a string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    # If last_name is not empty, print "My name is <first_name> <last_name>"
    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    # Otherwise, print "My name is <first_name>"
    else:
        print("My name is {}".format(first_name))
