#!/usr/bin/python3
def best_score(my_dict):
    if my_dict:
        newDict = sorted(my_dict, key=lambda k: int(my_dict[k]), reverse=True)
        return newDict[0]
    return None
