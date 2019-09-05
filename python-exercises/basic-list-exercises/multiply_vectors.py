def multiply_vectors(vector_one, vector_two):
    vector_product = []
    for i in range(0, len(vector_one)):
        vector_product.append(vector_one[i] * vector_two[i])
    return vector_product