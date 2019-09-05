def even_numbers(num_array):
    even_nums = []
    for num in num_array:
        if (num % 2 == 0):
            even_nums.append(num)
    return even_nums