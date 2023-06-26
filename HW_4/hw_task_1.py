# Напишите функцию для транспонирования матрицы

def trans_matrix(mat):
    new_matrix = [[0 for j in range(len(mat))] for i in range(len(mat[0]))] # находим размер новой матрицы
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            new_matrix[j][i] = mat[i][j]
    return new_matrix


matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix)
print(trans_matrix(matrix))