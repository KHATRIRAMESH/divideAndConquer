def min_max_da(A, low, high):
    if low == high:
        return A[low], A[low], 0
    elif high == low + 1:
        if A[low] < A[high]:
            return A[low], A[high], 1
        else:
            return A[high], A[low], 1
    mid = (low + high) // 2
    min1, max1, comp1 = min_max_da(A, low, mid)
    min2, max2, comp2 = min_max_da(A, mid + 1, high)

    overall_min = min(min1, min2)
    overall_max = max(max1, max2)

    comparisons = comp1 + comp2 + 2

    return overall_min, overall_max, comparisons


arr = [3, 5, 1, 8, 2, 7, 10]
min_val, max_val, comparisons = min_max_da(arr, 0, len(arr) - 1)
print(
    f"Divide and Conquer Approach: Min = {min_val}, Max = {max_val}, Comparisons = {comparisons}"
)


# time complexity = "O(n)"
# space complexity = "O(log n)" (due to recursion stack)
