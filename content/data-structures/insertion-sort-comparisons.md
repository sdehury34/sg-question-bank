---
title: Counting comparisons made by insertion sort on [5, 2, 4, 6, 1, 3]
subject: data-structures
topic: Sorting Algorithms
level: Poly / University
difficulty: Medium
description: Trace the standard insertion sort algorithm on a 6-element array and count the total number of key comparisons it performs.
date: 2026-07-15
---

## Question

Consider the standard insertion sort algorithm below, which counts one comparison every time it checks `arr[j] > key` (including the comparison that fails and stops the inner loop):

```python
def insertion_sort_count(arr):
    comparisons = 0
    n = len(arr)
    for i in range(1, n):
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
    return comparisons
```

How many comparisons does `insertion_sort_count` make when sorting the array `[5, 2, 4, 6, 1, 3]`?

## Solution

**Step 1 — Trace pass by pass.** Insertion sort builds up a sorted prefix one element at a time. For each new element (`key`), it is compared against elements to its left until it finds its correct position.

- **i = 1**, `key = 2`. Compare with `arr[0] = 5`: \(5 > 2\), shift 5 right (1 comparison). `j` becomes −1, loop stops. Array: `[2, 5, 4, 6, 1, 3]`.
- **i = 2**, `key = 4`. Compare with `arr[1] = 5`: \(5 > 4\), shift (1 comparison). Compare with `arr[0] = 2`: \(2 > 4\) is false, stop (1 comparison). Total this pass: 2. Array: `[2, 4, 5, 6, 1, 3]`.
- **i = 3**, `key = 6`. Compare with `arr[2] = 5`: \(5 > 6\) is false, stop (1 comparison). Total this pass: 1. Array unchanged: `[2, 4, 5, 6, 1, 3]`.
- **i = 4**, `key = 1`. Compare with `arr[3] = 6`, `arr[2] = 5`, `arr[1] = 4`, `arr[0] = 2` — all greater than 1, so all 4 shift (4 comparisons), then `j` reaches −1. Total this pass: 4. Array: `[1, 2, 4, 5, 6, 3]`.
- **i = 5**, `key = 3`. Compare with `arr[3] = 6`: shift (1). Compare with `arr[2] = 5`: shift (1). Compare with `arr[1] = 4`: shift (1). Compare with `arr[0] = 2`: \(2 > 3\) is false, stop (1). Total this pass: 4. Array: `[1, 2, 3, 4, 5, 6]`.

**Step 2 — Sum the comparisons per pass.**

$$1 + 2 + 1 + 4 + 4 = 12$$

**Step 3 — Check.** Running `insertion_sort_count([5, 2, 4, 6, 1, 3])` in Python confirms the function returns `12`, and the final array `[1, 2, 3, 4, 5, 6]` is correctly sorted, matching the hand trace above.

**Common mistake:** forgetting to count the final "failing" comparison that stops the inner `while` loop (e.g. the one comparison in the i = 3 pass) — every entry into the inner loop counts as one comparison, whether or not a shift happens as a result.

## Answer

`insertion_sort_count` makes **12** comparisons in total when sorting `[5, 2, 4, 6, 1, 3]`.
