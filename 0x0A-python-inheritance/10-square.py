#!/usr/bin/python3
"""Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Initializing Square obj
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    """
    Returns area of Square
    """
    def area(self):
        return self.__size * self.__size
