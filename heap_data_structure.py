# A binary heap is a complete binary tree that satisfies:
# 1. Min-Heap Property: The value of each node is less than or equal to the values of its children.
# 2. Max-Heap Property: The value of each node is greater than or equal to the values of its children.
# This implementation provides a Min-Heap.


# Array representation of the heap

# for node at index i:
# left child index = 2*i + 1
# right child index = 2*i + 2
# parent index = (i - 1) // 2
# what does // operator do in python?
# => The // operator in Python performs floor division, which means it divides two numbers and rounds down to the nearest whole number.


def max_heapify(Array, i, heap_size):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if left < heap_size and Array[left] > Array[largest]:
        largest = left

    if right < heap_size and Array[right] > Array[largest]:
        largest = right

    if largest != i:
        Array[i], Array[largest] = Array[largest], Array[i]
        max_heapify(Array, largest, heap_size)


def build_max_heap(Array):
    heap_size = len(Array)
    for i in range((heap_size // 2) - 1, -1, -1):
        max_heapify(Array, i, heap_size)


arr = [3, 1, 6, 5, 2, 4]
build_max_heap(arr)
print("Max-Heap array is:", arr)
