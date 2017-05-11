#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set1 = list(set(set_1) - set(set_2))
    set2 = list(set(set_2) - set(set_1))
    return (set1 + set2)
