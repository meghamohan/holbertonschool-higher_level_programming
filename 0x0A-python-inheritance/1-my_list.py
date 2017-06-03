#!/usr/bin/python3
"""The subclass MyList inherits from superclass list"""


class MyList(list):

    def print_sorted(self):
        print(sorted(self))
