#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    This is the say_my_name module
    This is a function that prints My name is {first_name} {last_name}
    """
    if (isinstance(first_name, str) is False or first_name is None):
        raise TypeError("first_name must be a string")
    if (isinstance(last_name, str) is False or last_name is None):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
