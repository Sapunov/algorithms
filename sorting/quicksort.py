import random


def partition(arr, lo, hi, asc=True):

    pivot = arr[hi]
    i = lo - 1

    if asc:
        for j in range(lo, hi):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
    else:
        for j in range(lo, hi):
            if arr[j] >= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[hi] = arr[hi], arr[i+1]

    return i+1


def rand_partition(arr, lo, hi, asc):

    idx = random.randint(lo, hi)
    arr[idx], arr[hi] = arr[hi], arr[idx]

    return partition(arr, lo, hi, asc)


def qsort(arr, *, lo=0, hi=None, asc=True):

    if hi is None: hi = len(arr) - 1
    if lo < hi:
        pivot = rand_partition(arr, lo, hi, asc)
        qsort(arr, lo=lo, hi=pivot-1, asc=asc)
        qsort(arr, lo=pivot+1, hi=hi, asc=asc)
