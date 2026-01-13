## Time Complexity Comparison

| Algorithm             | Best      | Average   | Worst            | Remarks                     |
| --------------------- | --------- | --------- | ---------------- | --------------------------- |
| Binary Search         | O(1)      | O(logn)   | O(logn)          | Requires sorted array       |
| Min-Max               | O(n)      | O(n)      | O(n)             | Optimal: 3n/2-2 comparisons |
| Merge Sort            | O(n logn) | O(n logn) | O(n logn)        | Stable, O(n) space          |
| Quick Sort            | O(n logn) | O(n logn) | O(n<sup>2</sup>) | In-place, cache friendly    |
| Randomized Quick Sort | O(n logn) | O(n logn) | O(n<sup>2</sup>) | Practically good            |
| Heap sort             | O(n logn) | O(n logn) | O(n logn)        | In-place, not stable        |
| Quick Select          | O(n)      | O(n)      | O(n<sup>2</sup>) | Expected linear time        |
| Median of Medians     | O(n)      | O(n)      | O(n)             | Worst-case linear time      |

#### When to use which algorithm?

1. Sorting small array(< 10 elements): insertion sort
2. Sorting large array : Quicksort ( generally fastest in practice)
3. need stability: merge sort
4. Memory Constrained: Heap sort
5. External sorting: Merge sort
6. finding Median: QuickSelect (expected linear) or median of Medians (guaranteed linear)
7. Searching sorted data: binary search

### ADVANCED TOPICS AND OPTIMIZATIONS

Parallel Divide and Conquer

    . Merge Sort: Easy to parallelize (merge parallel halves)

    . Quick Sort: Can parallelize partitions

    Binary Search: Difficult to parallelize effectively

Cache-Oblivious Algorithms

    Algorithms that optimize cache usage without knowing cache parameters

    Cache-oblivious Merge Sort: Uses recursive subdivision

    Cache-oblivious Matrix Multiplication: Improves locality

External Memory Algorithms

    For data too large to fit in RAM

    External Merge Sort: Uses disk I/O efficiently

    B-trees: Optimized for disk access

Probabilistic Analysis

    Randomized algorithms: Use randomization to avoid worst case

    Expected running time: Average over random choices

    High probability bounds: Probability of bad case is negligible

Amortized Analysis

    For data structures where operations vary in cost

    Aggregate method: Total cost divided by operations

    Accounting method: Assign credits to operations

    Potential method: Use potential function
