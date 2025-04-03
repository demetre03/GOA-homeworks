def squared(list):
    new_list = []
    for i in list:
        i = i ** 2
        new_list.append(i)
    return new_list

print(squared([2, 4, 5, 7]))