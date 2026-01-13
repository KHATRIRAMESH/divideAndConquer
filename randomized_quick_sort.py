import random

from quick_sort import partition


def randomized_quick_sort(arr, low, high):
    random_index = random.randint(low, high)

    # Swap the randomly chosen pivot with the last element

    arr[random_index], arr[high] = arr[high], arr[random_index]

    return partition(arr, low, high)


arr = [10, 7, 8, 9, 1, 5]
randomized_quick_sort(arr, 0, len(arr) - 1)
