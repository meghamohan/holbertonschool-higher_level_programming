#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if (my_list is not None and len(my_list) > 0):
        size = len(my_list)
        for i in range(size - 1, -1, -1):
            print("{:d}".format(my_list[i]))
