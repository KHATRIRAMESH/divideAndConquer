def merge_sort(A, low, high):
    if low < high:
        mid = (low + high) // 2

        # divide and conquer
        merge_sort(A, low, mid)
        merge_sort(A, mid + 1, high)
        merge(A, low, mid, high)


def merge(A, low, mid, high):
    # Create temporary arrays
    left = A[low : mid + 1]
    right = A[mid + 1 : high + 1]

    i = 0  # Initial index of first sub-array
    j = 0  # Initial index of second sub-array
    k = low  # Initial index of merged sub-array

    # Merge the temp arrays back into A[low..high]
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
        k += 1

    # Copy the remaining elements of left[], if there are any
    while i < len(left):
        A[k] = left[i]
        i += 1
        k += 1

    # Copy the remaining elements of right[], if there are any
    while j < len(right):
        A[k] = right[j]
        j += 1
        k += 1


arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr, 0, len(arr) - 1)
print("Sorted array is:", arr)


# time complexity = "O(n log n)"
# space complexity = "O(n)" (due to temporary arrays)

# stable sort = "Yes"
# not in-place: requires O(n) extra space
# external sorting: can sort data too large to fit in memory
# parallelizable: can be adapted for parallel processing
# what is stable sort?
# => A stable sort maintains the relative order of records with equal keys (i.e., values).
