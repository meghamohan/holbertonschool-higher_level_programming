#!/usr/bin/python3


class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value <= 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        errorMsg = "position must be a tuple of 2 positive integers"
        if type(value) is not tuple:
            raise TypeError(errorMsg)
        if len(value) < 2:
            raise TypeError(errorMsg)
        if not (type(value[0]) is int and type(value[1]) is int):
            raise TypeError(errorMsg)
        if (value[0] < 0 or value[1] < 0):
            raise TypeError(errorMsg)
        self.__position = value

    def area(self):
        return (self.size * self.size)

    def my_print(self):
        if self.size == 0:
            print()
        else:
            print(self.__position[1] * '\n', end='')
            for i in range(self.size):
                print(self.__position[0] * ' ', end='')
                for j in range(self.size):
                    print('#', end='')
                print()
