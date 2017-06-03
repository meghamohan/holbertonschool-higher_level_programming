#!/usr/bin/python3
""" function that appends a string at the end of a text file
 (UTF8) and returns the number of characters added """


def append_write(filename="", text=""):
    with open(filename, 'a') as file1:
        return file1.write(text)
