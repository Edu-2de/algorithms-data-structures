def insertion_sort(list):

    for i in range (1, len(list)):
        actual_item = list[i]
        j = i - 1

        while j>=0 and list[j] > actual_item:
            list[j + 1] = list[j]

            j = j - 1
        list[j + 1] = actual_item
    print(list)
        

list = [1, 3, 4, 2]
insertion_sort(list)
