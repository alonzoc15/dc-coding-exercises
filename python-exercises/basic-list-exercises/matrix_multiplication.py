sample_matrix_one = [
    [1,2],
    [3,4],
    [5,6]
]

sample_matrix_two = [
    [7,8,9],
    [10,11,12]
]

sample_matrix_three = [[4,6,8],[2,1,4],[6,9,3],[8,1,4]]

sample_matrix_four = [[1,7,6,4],[8,9,2,3],[3,4,8,9]] 

def multiply_matrices(matrix_one, matrix_two):
    MATRIX_ONE_ROW_NUM = len(matrix_one)
    MATRIX_ONE_COL_NUM = len(matrix_one[0])
    MATRIX_TWO_ROW_NUM = len(matrix_two)
    MATRIX_TWO_COL_NUM = len(matrix_two[0])

    matrix_product = []
    matrix_product_row = []
    matrix_product_entry_summands = []
    # iterate through each row of the first matrix
    for i in range(MATRIX_ONE_ROW_NUM):
        # grab a single row from the first matrix
        matrix_one_row = matrix_one[i]
        for j in range(MATRIX_TWO_COL_NUM):
            for k in range(MATRIX_ONE_COL_NUM):
                matrix_product_entry_summands.append(matrix_one_row[k] * matrix_two[k][j])
            matrix_product_row.append(sum(matrix_product_entry_summands))
            matrix_product_entry_summands = []
        matrix_product.append(matrix_product_row)
        matrix_product_row = []
            
    return matrix_product

# print(multiply_matrices(sample_matrix_one,sample_matrix_two))
print(multiply_matrices(sample_matrix_three,sample_matrix_four))

