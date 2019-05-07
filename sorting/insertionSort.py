def insertion_sort(array, ascending=True):

    for i in range(1, len(array)):
        j = i - 1
        value = array[i]

        if ascending:
            while value < array[j] and j >= 0:
                array[j + 1] = array[j]
                j -= 1
        else:
            while value > array[j] and j >= 0:
                array[j + 1] = array[j]
                j -= 1

        array[j + 1] = value
