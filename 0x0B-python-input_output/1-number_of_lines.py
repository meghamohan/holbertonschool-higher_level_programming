#!/usr/bin/python3
""" function that returns the number of lines of a text file """


def number_of_lines(filename=""):
    count = 0
    with open(filename) as file1:
        for line in file1:
            count += 1
    return count
