def quick_sort(A, low, high):
    if low < high:
        pi = partition(A, low, high)

        # Recursively sort elements before
        # partition and after partition
        quick_sort(A, low, pi - 1)
        quick_sort(A, pi + 1, high)


def partition(A, low, high):
    pivot = A[high]  # pivot
    i = low - 1  # Index of smaller element

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if A[j] <= pivot:
            i = i + 1
            A[i], A[j] = A[j], A[i]  # swap
    A[i + 1], A[high] = A[high], A[i + 1]  # swap
    return i + 1


arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array is:", arr)

# time complexity = "O(n log n)" on average, "O(n^2)" in worst case
# space complexity = "O(log n)" (due to recursion stack)
# stable sort = "No"
# in-place: requires only a small, constant amount of additional storage space
# external sorting: can sort data too large to fit in memory with modifications
# parallelizable: can be adapted for parallel processing with modifications
