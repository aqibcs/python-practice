def binary_search(list, target):
    first = 0
    last = len(list) - 1

    # Repeat until the pointers low and high meet each other.
    while first <= last:
        midpoint = (first + last)

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return -1


def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("target not found in list")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = binary_search(numbers, 5)

verify(result)
