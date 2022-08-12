import numpy as np


def gauss(matrix):
    matrix = np.array(matrix)

    for nrow in range(len(matrix)):
        # nrow equal term number
        # np.argmax return term number with max element in smaller matrix
        # is started from nrow. So should add nrow to result
        pivot = nrow + np.argmax(abs(matrix[nrow:, nrow]))
        if pivot != nrow:
            # swap
            # matrix[nrow], matrix[pivot] = matrix[pivot], matrix[nrow] - don`t work.

            matrix[[nrow, pivot]] = matrix[[pivot, nrow]]
        row = matrix[nrow]
        divider = row[nrow]  # diagonal element
        if abs(divider) < 1e-10:
            # It makes no sense to continue
            return matrix
        # divide by a diagonal element
        row /= divider
        # now it is necessary to subtract the given term from all the underlying lines
        for lower_row in matrix[nrow+1:]:
            factor = lower_row[nrow]  # row element in the nrow
            lower_row -= row*factor  # subtract to get a zero in the nrow column

    return [[j for j in i] for i in matrix]
