#!/usr/bin/python3
""" rebel int class that inherits from int"""


class MyInt(int):
    def __eq__(self, other):
        return False

    def __ne__(self, other):
        return True
