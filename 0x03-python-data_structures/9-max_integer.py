#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return "None"
    length = len(my_list) - 1
    mValue = my_list[length]
    while(length >= 0):
        if mValue < my_list[length]:
            mValue = my_list[length]
        length -= 1
    return mValue
