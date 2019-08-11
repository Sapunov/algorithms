def qsort(array, reverse=False):

    la = len(array)

    if la >= 2:
        mid = la // 2
        pivot = array[mid]
        less = [array[i] for i in range(la) if array[i] <= pivot and i != mid]
        greater = [array[i] for i in range(la) if array[i] > pivot and i != mid]

        if reverse:
            return qsort(greater, reverse) + [pivot] + qsort(less, reverse)
        return qsort(less, reverse) + [pivot] + qsort(greater, reverse)
    else:
        return array
