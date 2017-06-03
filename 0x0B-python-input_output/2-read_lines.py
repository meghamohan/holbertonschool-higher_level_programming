#!/usr/bin/python3
""" function that reads n lines of a text
 file (UTF8) and prints it to stdout """


def read_lines(filename="", nb_lines=0):
    with open(filename, 'r', encoding="UTF8") as file1:
        if nb_lines > len(list(file1)) or nb_lines <= 0:
            file1.seek(0)
            print(file1.read(), end='')
        else:
            file1.seek(0)
            while nb_lines > 0:
                print(file1.readline(), end='')
                nb_lines -= 1
