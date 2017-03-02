def linear_search(list_of_items, searched_elem):

    for i, value in enumerate(list_of_items):
        if value == searched_elem:
            return i

    return -1
