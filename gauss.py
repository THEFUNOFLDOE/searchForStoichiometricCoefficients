import numpy as np


def gauss(matrix):
    matrix = np.array(matrix)
    # matrix = matrix_filter(matrix)

    for nrow in range(len(matrix)):
        # nrow равен номеру строки
        # np.argmax возвращает номер строки с максимальным элементом в уменьшенной матрице
        # которая начинается со строки nrow. Поэтому нужно прибавить nrow к результату
        pivot = nrow + np.argmax(abs(matrix[nrow:, nrow]))
        if pivot != nrow:
            # swap
            # matrix[nrow], matrix[pivot] = matrix[pivot], matrix[nrow] - не работает.
            # нужно переставлять строки именно так, как написано ниже
            matrix[[nrow, pivot]] = matrix[[pivot, nrow]]
        row = matrix[nrow]
        divider = row[nrow] # диагональный элемент
        if abs(divider) < 1e-10:
            # почти нуль на диагонали. Продолжать не имеет смысла, результат счёта неустойчив
            return matrix
        # делим на диагональный элемент.
        row /= divider
        # теперь надо вычесть приведённую строку из всех нижележащих строчек
        for lower_row in matrix[nrow+1:]:
            factor = lower_row[nrow] # элемент строки в колонке nrow
            lower_row -= row*factor # вычитаем, чтобы получить ноль в колонке nrow
    # приводим к диагональному виду

    return [[j for j in i] for i in matrix]


def matrix_filter(matrix):
    delete_list = []
    for i in range(len(matrix)):
        row = matrix[i]
        irow = 0
        if row[0] == 0:
            for im, m in enumerate(row):
                if m != 0:
                    irow = im
                    break
        for index, j in enumerate(matrix):
            point = 0
            if i == index:
                continue

            if j[0] == 0:
                for ig, g in enumerate(j):
                    if g != 0:
                        point = ig
                        break

            if row[irow]/j[point] == int(row[irow]/j[point]):
                j = [g for g in np.array(j)*int(row[irow]/j[point])]
                if row == j:
                    delete_list.append(index)

            elif j[point]/row[irow] == int(j[point]/row[irow]):

                row = [g for g in np.array(row) * int(j[point]/row[irow])]
                if row == j:
                    delete_list.append(i)

    for i in set(delete_list):
        del matrix[i]

    return np.array(matrix)


def make_identity(matrix):
    for nrow in range(len(matrix)-1, 0, -1):
        row = matrix[nrow]
        for upper_row in matrix[:nrow]:
            factor = upper_row[nrow]
            upper_row -= factor*row
    return matrix
