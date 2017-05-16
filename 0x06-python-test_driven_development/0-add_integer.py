#!/usr/bin/python3
"""
a and b must be integers or floats, otherwise raise a TypeError 
exception with the message 'a must be an integer' or 'b must be an integer'
should be raised
a and b must be first casted to integers if they are float
Returns an integer: the addition of a and b

"""
def add_integer(a, b):
        if isinstance(a, (int, float)) is not True:
            raise TypeError('a must be an integer')
        elif isinstance(b, (int, float)) is not True:
            raise TypeError('b must be an integer')
        return(int(a) + int(b))
