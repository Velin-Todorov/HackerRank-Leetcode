#!/usr/bin/python3

def diagonalSum(mat):

    sum_mat = 0
    mid = 0

    if len(mat[0]) % 2 != 0:
        
        middle = int(len(mat[0]) / 2)

        mid = mat[middle][middle]

    if len(mat) == 1:
        return mat[0][0]
    
    for i in range(len(mat)):
        sum_mat += mat[i][i]
        sum_mat += mat[i][len(mat) - i - 1]

    sum_mat -= mid

    return sum_mat
