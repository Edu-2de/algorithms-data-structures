def selection_sort(list):
    if not list:
        return list
    for i in range(len(list)):
        min_i = i
        for j in range(i + 1, len(list)):
            if list[j] < list[min_i]:
                min_i = j
        list[i], list[min_i] = list[min_i], list[i]

    print(list)


selection_sort([2, 4, 3, 6, 9, 1, 6, 3])
