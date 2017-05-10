#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newList = []
    l = 0
    while l < len(my_list):
        if my_list[l] % 2 == 0:
            newList.append(True)
        else:
            newList.append(False)
        l += 1
    return newList
