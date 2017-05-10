#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length > 0:
        firstChar = sentence[0]
    else:
        firstChar = "None"
    tup = (length, firstChar)
    return tup
