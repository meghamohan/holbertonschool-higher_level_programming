#!/usr/bin/python3
def simple_delete(my_dict, key=""):
    dictCopy = dict(my_dict)
    if key in dictCopy:
        del dictCopy[key]
    return dictCopy
