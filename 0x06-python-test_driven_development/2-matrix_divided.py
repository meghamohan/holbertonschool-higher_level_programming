#!/usr/bin/python3
"""
- This function divides all elements of a matrix
- matrix must be a list of lists of integers or floats,
otherwise a TypeError exception with the message is raised
- Each row of the matrix must be of the same size,
otherwise raise a TypeError exception with the message
- div must be a number (integer or float),otherwise raise a TypeError
- div can't be equal to 0, otherwise raise a ZeroDivisionError exception 
"""
def matrix_divided(matrix, div):
    if isinstance(div, (int,float)) is False:
        raise TypeError("div must be a number")
    elif div is 0:
        raise ZeroDivisionError("division by zero")
    if matrix is None or len(matrix) is 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/float")
    for row in matrix:
        if len(row) is not len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    for row in matrix:
        for ele in range(len(row)):
            if not isinstance(row[ele], (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    return [[round(row[i] / div, 2) for i in range(len(row))] for row in matrix] 
