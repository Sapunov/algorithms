def merge(array, left, right, ascending):

    i = j = 0

    if ascending:
        while i + j < len(array):
            if j == len(right) or (i < len(left) and left[i] < right[j]):
                array[i + j] = left[i]
                i += 1
            else:
                array[i + j] = right[j]
                j += 1
    else:
        while i + j < len(array):
            if j == len(right) or (i < len(left) and left[i] > right[j]):
                array[i + j] = left[i]
                i += 1
            else:
                array[i + j] = right[j]
                j += 1


def merge_sort(array, ascending=True):

    r = len(array)

    if r >= 2:
        q = r // 2
        left, right = array[:q], array[q:]

        merge_sort(left, ascending)
        merge_sort(right, ascending)

        merge(array, left, right, ascending)
