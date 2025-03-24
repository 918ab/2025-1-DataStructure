def move_zeros(a_list):
    zero_index = 0
    for index, n in enumerate(a_list):
        if n != 0:
            a_list[zero_index] = n
            if zero_index != index:
                a_list[index] = 0
            zero_index += 1
    return (a_list)

a_list = [8,0,3,0,12]
move_zeros(a_list)
print(a_list)

# index 0 / n 8 / zero_index 1 / a_list [8,0,3,0,12]
# index 1 / n 0 / zero_index 1 / a_list [8,0,3,0,12]
# index 2 / n 3 / zero_index 2 / a_list [8,3,0,0,12]
# index 3 / n 0 / zero_index 2 / a_list [8,3,0,0,12]
# index 4 / n 12 / zero_index 3 / a_list [8,3,12,0,0]
