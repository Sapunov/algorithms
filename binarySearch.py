# TODO: now it works only for sorted and uniqued sequences
#       It should work for not only uniq sequences to find out first hit

def binary_search(sorted_list, searched_elem):

    left = 0
    right = len(sorted_list) - 1

    while right >= left:
        mid = (right + left) // 2

        if sorted_list[mid] == searched_elem:
            return mid

        if mid > searched_elem:
            right = mid - 1
        else:
            left = mid + 1

    return -1
