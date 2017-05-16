#!/usr/bin/python3
def print_square(size):
    """
    This is print_square module
    This is a function that prints a square with the character #
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
