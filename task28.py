def remove_duplicates(lst):
    unique_elements = []
    for item in lst:
        if item not in unique_elements:
            unique_elements.append(item)
    return unique_elements
original_list = [3, 5, 1, 3, 7, 5, 9, 1, 3, 5]
unique_list = remove_duplicates(original_list)
print(unique_list)