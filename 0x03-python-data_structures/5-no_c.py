#!/usr/bin/python3
def no_c(str):
    newString = ""
    for i in str:
        if not (i == 'c' or i == 'C'):
            newString += i
    return newString
