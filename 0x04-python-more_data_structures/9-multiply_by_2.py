#!/usr/bin/python3
def multiply_by_2(my_dict):
    newDict = {}
    for i in my_dict.keys():
        newDict[i] = my_dict[i] * 2
    return newDict
