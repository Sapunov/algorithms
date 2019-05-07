def swap(array, a, b):

    array[a], array[b] = array[b], array[a]


def subarray_min_index(array, start):

    min_index = start
    min_value = array[start]

    for i in range(start + 1, len(array)):
        if array[i] < min_value:
            min_value = array[i]
            min_index = i

    return min_index


def subarray_max_index(array, start):

    max_index = start
    max_value = array[start]

    for i in range(start + 1, len(array)):
        if array[i] > max_value:
            max_value = array[i]
            max_index = i

    return max_index


def selection_sort(array, ascending=True):

    if ascending:
        for i in range(len(array) - 1):
            swap(array, i, subarray_min_index(array, i))
    else:
        for i in range(len(array) - 1):
            swap(array, i, subarray_max_index(array, i))
