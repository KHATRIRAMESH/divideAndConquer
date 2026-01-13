def naive_min_max(arr):
    min_val = max_val = arr[0]

    comparisons = 0

    for num in range(1, len(arr)):
        comparisons += 1
        if arr[num] < min_val:
            min_val = arr[num]
        else:
            comparisons += 1
            if arr[num] > max_val:
                max_val = arr[num]
    return min_val, max_val, comparisons


arr = [3, 5, 1, 8, 2, 7, 10]
min_val, max_val, comparisons = naive_min_max(arr)
print(f"Naive Approach: Min = {min_val}, Max = {max_val}, Comparisons = {comparisons}")
