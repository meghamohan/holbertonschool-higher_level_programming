#!/usr/bin/python3
""" function that reads a text file (UTF8) and prints it to stdout """


def read_file(filename=""):
    with open(filename, 'r') as file1:
        readFile = file1.read()
    print("{:s}".format(readFile), end='')
