#!/usr/bin/python3
"""The subclass MyList inherits from superclass list"""


class MyList(list):
    def __init__(self):
        pass

    def print_sorted(self):
        print(sorted(self))
