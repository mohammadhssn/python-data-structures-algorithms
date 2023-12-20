def merge(list1: list, list2: list) -> list:
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1

    while i < len(list1):
        combined.append(list1[i])
        i += 1

    while j < len(list2):
        combined.append(list2[j])
        j += 1

    return combined


def merge_sort(my_list: list) -> list:
    if len(my_list) == 1:
        return my_list
    mid_index = len(my_list) // 2
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])

    return merge(left, right)


original_list = [3, 1, 4, 2]

sorted_list = merge_sort(original_list)

print('Original List:', original_list)

print('\nSorted List:', sorted_list)


"""
    EXPECTED OUTPUT:
    ----------------
    Original List: [3, 1, 4, 2]

    Sorted List: [1, 2, 3, 4]

 """
