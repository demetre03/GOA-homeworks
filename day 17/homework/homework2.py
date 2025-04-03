def even (list):
    new_list = []
    for i in list:
        if i % 2 == 0:
            new_list.append(i)
    return new_list

print(even([13, 14, 50, 60, 57]))