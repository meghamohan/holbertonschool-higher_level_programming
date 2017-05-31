#!/usr/bin/python3
"""superclass for rectangle"""


class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        try:
            return (self.__width * self.__height)
        except:
            return (self.size ** 2)

    def __str__(self):
        return ("[{}] {}/{}".format(
            self.__class__.__name__, self.__width, self.__height))


class Square(Rectangle):
    def __init__(self, size):
        self.__size = size
        super().__init__(self.__size, self.__size)
