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

    return left, right


def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process
    :param left:
    :param right:
    :return: return a new merged list
    """

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l


def verify_sorted(lst):
    n = len(lst)

    if n == 0 or n == 1:
        return True

    return lst[0] < lst[1] and verify_sorted(lst[1:])


alist = [54, 26, 93, 27, 77, 31, 44, 54]
l = merge_sort(alist)
print(verify_sorted(alist))
print(verify_sorted(l))
