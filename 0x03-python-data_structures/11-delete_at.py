#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if not (my_list is None or idx < 0):
        del my_list[idx]
    return my_list
