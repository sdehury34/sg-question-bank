---
title: Number of comparisons made by insertion sort on [5, 2, 4, 6, 1, 3]
subject: data-structures
topic: Sorting Algorithms
level: Poly / University
difficulty: Medium
description: Trace insertion sort pass by pass on a 6-element array and count the exact number of key comparisons it performs.
date: 2026-07-14
---

## Question

Trace the standard insertion sort algorithm on the array

$$[5, 2, 4, 6, 1, 3]$$

For each pass \(i = 1, 2, \dots, 5\) (0-indexed, inserting element at index \(i\) into the sorted prefix), state the array after the pass and the number of comparisons made during that pass. Count a "comparison" as each time the algorithm checks whether the current key is smaller than the element to its left (including the final check that fails and stops the shift). Give the total number of comparisons for the whole sort.

## Solution

Insertion sort builds up a sorted prefix one element at a time. For each new element (the "key"), it shifts larger elements in the sorted prefix one position right until it finds the key's correct spot, comparing the key against each shifted element along the way.

**Pass \(i=1\), key = 2:** compare with 5. \(5 > 2\), so shift 5 right and insert 2 at the front.
Array: \([2, 5, 4, 6, 1, 3]\). Comparisons: 1.

**Pass \(i=2\), key = 4:** compare with 5. \(5 > 4\), shift. Compare with 2. \(2 > 4\) is false, stop; insert 4 after 2.
Array: \([2, 4, 5, 6, 1, 3]\). Comparisons: 2.

**Pass \(i=3\), key = 6:** compare with 5. \(5 > 6\) is false, stop immediately; 6 stays in place.
Array: \([2, 4, 5, 6, 1, 3]\). Comparisons: 1.

**Pass \(i=4\), key = 1:** compare with 6 (shift), 5 (shift), 4 (shift), 2 (shift) — all greater than 1 — then reach the start of the array (no more elements to compare), so the shifting stops after 4 comparisons; 1 is inserted at the front.
Array: \([1, 2, 4, 5, 6, 3]\). Comparisons: 4.

**Pass \(i=5\), key = 3:** compare with 6 (shift), 5 (shift), 4 (shift), then 2. \(2 > 3\) is false, stop; insert 3 after 2.
Array: \([1, 2, 3, 4, 5, 6]\). Comparisons: 4.

**Total comparisons:** \(1 + 2 + 1 + 4 + 4 = 12\).

**Verification by running the algorithm in code** (Python, counting exactly as defined above):

```python
def insertion_sort_count(arr):
    arr = arr[:]
    comparisons = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key
    return arr, comparisons

print(insertion_sort_count([5, 2, 4, 6, 1, 3]))
# ([1, 2, 3, 4, 5, 6], 12)
```

Running this confirms the sorted array \([1, 2, 3, 4, 5, 6]\) and a total of **12** comparisons, matching the manual trace.

**Common mistake:** stopping the count at the last *successful* shift and forgetting to count the final comparison that fails and ends the while-loop (e.g. counting pass \(i=2\) as 1 comparison instead of 2). That final failed comparison is what tells the algorithm where to stop, so it must be counted.

## Answer

Sorted array: \([1, 2, 3, 4, 5, 6]\). Total comparisons: **12**.
