#!/usr/bin/python3
def square_matrix_simple(matrix):
    # Create an empty list to store the new matrix
    new_matrix = []
    # Iterate over each row
    for row in matrix:
        # Use map to apply lambda to each element in the row
        # The lambda function squares each element
        new_row = list(map(lambda element: element ** 2, row))
        # Append the new row to the new matrix
        new_matrix.append(new_row)
    return new_matrix
