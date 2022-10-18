def merge_sort(lst):
    """
    sort a list in ascending order
    Return a new sorted list

    Divide: find the point of the list and divide into sublist
    Conquer: recursively sort the sublist created in the previous step
    Combine: Merge the sorted sublist created in the previous step
    """

    if len(lst) <= 1:
        return lst

    left_half, right_half = split(lst)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(lst):
    """
    divide the unsorted list at midpoint
    :param lst:
    :return: two sublist left and right
    """

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
