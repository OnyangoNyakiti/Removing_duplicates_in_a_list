numbers = [5, 2, 2, 3, 5, 7, 1, 7, 4, 7]
unique_list = []
for item in numbers:
    if item not in unique_list:
        unique_list.append(item)
print(unique_list)