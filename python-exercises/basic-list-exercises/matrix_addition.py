sample_matrix_one = [
    [1,3],
    [2,4]
]

sample_matrix_two = [
    [5,2],
    [1,0]
]

def add_matrices(matrix_one, matrix_two):
    row_num = len(matrix_one)
    col_num = len(matrix_one[0])
    matrix_sum = []

    for i in range(0, row_num):
        matrix_row_sum = []
        for j in range(0, col_num):
            matrix_row_sum.append(matrix_one[i][j] + matrix_two[i][j])
        matrix_sum.append(matrix_row_sum)

    return matrix_sum

print(add_matrices(sample_matrix_one,sample_matrix_two))