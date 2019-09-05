def smallest_number(num_array):
    smallest_num = num_array[0]
    for num in num_array:
        if smallest_num > num:
            smallest_num = num
    return smallest_num