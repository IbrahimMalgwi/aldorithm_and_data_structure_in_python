def recursive_binary_search(lst, target):
    if len(lst) == 0:
        return False
    else:
        midpoint = (len(lst)) // 2

        if lst[midpoint] == target:
            return True
        else:
            if lst[midpoint] < target:
                return recursive_binary_search(lst[midpoint + 1:], target)
            else:
                return recursive_binary_search(lst[:midpoint], target)


def verify(result):
    print("target found", result)


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = recursive_binary_search(numbers, 12)
verify(result)

result = recursive_binary_search(numbers, 6)
verify(result)

result = recursive_binary_search(numbers, 2)
verify(result)
