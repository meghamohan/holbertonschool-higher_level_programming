#!/usr/bin/python3
""" function that writes a string to a text file (UTF8)
 and returns the number of characters written """


def write_file(filename="", text=""):
    with open(filename, 'w') as file1:
        return file1.write(text)
