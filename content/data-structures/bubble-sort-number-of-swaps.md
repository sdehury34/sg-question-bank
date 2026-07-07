---
title: Counting the number of swaps performed by bubble sort on [5, 1, 4, 2, 8]
subject: data-structures
topic: Sorting Algorithms
level: Poly / University
difficulty: Medium
description: Trace bubble sort with an early-exit optimisation on the array [5, 1, 4, 2, 8] and count the total number of swaps performed.
date: 2026-07-08
---

## Question

Consider this bubble sort with an early-exit optimisation (it stops as soon as a full pass makes no swaps):

```python
def bubble_sort(arr):
    n = len(arr)
    swaps = 0
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return swaps
```

Trace `bubble_sort` on the array `[5, 1, 4, 2, 8]`. How many swaps are performed in total, and how many full passes over the array are made before the function returns?

## Solution

**Pass 1 (\(i=0\), compares \(j=0\) to \(3\)):** start `[5, 1, 4, 2, 8]`

- \(j=0\): \(5 > 1\) → swap → `[1, 5, 4, 2, 8]`
- \(j=1\): \(5 > 4\) → swap → `[1, 4, 5, 2, 8]`
- \(j=2\): \(5 > 2\) → swap → `[1, 4, 2, 5, 8]`
- \(j=3\): \(5 > 8\)? No → no swap

Pass 1 makes 3 swaps. Array is now `[1, 4, 2, 5, 8]`.

**Pass 2 (\(i=1\), compares \(j=0\) to \(2\)):** start `[1, 4, 2, 5, 8]`

- \(j=0\): \(1 > 4\)? No
- \(j=1\): \(4 > 2\) → swap → `[1, 2, 4, 5, 8]`
- \(j=2\): \(4 > 5\)? No

Pass 2 makes 1 swap. Array is now `[1, 2, 4, 5, 8]`.

**Pass 3 (\(i=2\), compares \(j=0\) to \(1\)):** start `[1, 2, 4, 5, 8]`

- \(j=0\): \(1 > 2\)? No
- \(j=1\): \(2 > 4\)? No

No swaps occur in pass 3, so `swapped` stays `False` and the loop breaks early.

**Total:** \(3 + 1 + 0 = 4\) swaps, over 3 full passes (the third pass detects the array is already sorted and exits early, instead of running all \(n-1 = 4\) passes).

**Verification by running the code:**

```
>>> bubble_sort([5, 1, 4, 2, 8])
4
```

which matches the hand trace above, and the final array `[1, 2, 4, 5, 8]` is correctly sorted.

**Common mistake:** counting *comparisons* instead of *swaps* (there are \(4+3+2=9\) comparisons across the three passes, not 4), or assuming the early-exit optimisation means only 2 passes run — the third pass still executes fully (making the comparisons) in order to discover that no swap is needed before breaking.

## Answer

4 swaps are performed, over 3 full passes (the third pass makes no swaps and triggers early exit).
