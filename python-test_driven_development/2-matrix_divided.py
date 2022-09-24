#!/usr/bin/python3
''' matrix_divided is a module that divides all elements of a matrix '''

def matrix_divided(matrix, div):
    ''' the module checks for type/ value of matriz and divisor before returning list'''
    if not isinstance(matrix, list): # see if matrix is a list
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (float, int)): # right type of divisor
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    for row in matrix:
        if isinstance(row, list) is False: # row = inner(supposed) list of matrix
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if (len(row)) != len(matrix[0]): # same size for every list inside matrix
            raise TypeError("Each row of the matrix must have the same size")

    '''map will iterate each element(i) of the iterable given (mat_list),
    applying the function lambda, which divides the element with div
    and it rounds the result to 2 decimal places(second argument of
    round), all inside a loop iterating each row(inner lists)'''
    divided_matrix = [list(map(lambda i: round(i / div, 2), mat_list)) for mat_list in matrix]
    return divided_matrix
