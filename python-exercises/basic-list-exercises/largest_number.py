def largest_number(num_array):
    largest_num = num_array[0]
    for num in num_array:
        if largest_num < num:
            largest_num = num
    return largest_num