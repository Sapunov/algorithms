def quick_sort(array, ascending=True):

    la = len(array)

    if la >= 2:
        mid = la // 2
        pivot = array[mid]
        less = [array[i] for i in range(la) if array[i] <= pivot and i != mid]
        greater = [array[i] for i in range(la) if array[i] > pivot and i != mid]

        if ascending:
            return quick_sort(less, ascending) + [pivot] + quick_sort(
                greater, ascending)
        else:
            return quick_sort(greater, ascending) + [pivot] + quick_sort(
                less, ascending)
    else:
        return array
