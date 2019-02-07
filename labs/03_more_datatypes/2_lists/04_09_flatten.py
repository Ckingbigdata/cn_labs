flattened_list = []
starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for sublist in starting_list:
    for val in sublist:
        flattened_list.append(val)
print(flattened_list)
