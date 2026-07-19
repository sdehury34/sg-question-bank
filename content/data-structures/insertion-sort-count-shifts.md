---
title: Counting element shifts performed by insertion sort
subject: data-structures
topic: Sorting Algorithms
level: Poly / University
difficulty: Medium
description: Trace insertion sort on a 6-element array by hand and count the total number of element shifts needed to sort it ascending.
date: 2026-07-20
---

## Question

Trace the insertion sort algorithm on the array `[5, 2, 9, 1, 5, 6]`, sorting it into ascending order. Count the total number of element **shifts** performed (each time an element is moved one position to the right to make room for the key being inserted counts as one shift).

## Solution

Insertion sort builds the sorted portion of the array one element at a time. For each new "key" element, it shifts every larger element in the sorted portion one place to the right until it finds the key's correct position.

Starting array: `[5, 2, 9, 1, 5, 6]` (index 0 to 5).

- **i = 1, key = 2:** Compare with `a[0] = 5`. Since `5 > 2`, shift 5 right (1 shift). Insert 2 at index 0.
  Array: `[2, 5, 9, 1, 5, 6]`
- **i = 2, key = 9:** Compare with `a[1] = 5`. Since `5 > 9` is false, no shift needed (0 shifts).
  Array: `[2, 5, 9, 1, 5, 6]`
- **i = 3, key = 1:** Compare with `a[2] = 9` (shift), `a[1] = 5` (shift), `a[0] = 2` (shift) — 3 shifts. Insert 1 at index 0.
  Array: `[1, 2, 5, 9, 5, 6]`
- **i = 4, key = 5:** Compare with `a[3] = 9` (shift). Compare with `a[2] = 5`: since `5 > 5` is false, stop — 1 shift. Insert 5 at index 3.
  Array: `[1, 2, 5, 5, 9, 6]`
- **i = 5, key = 6:** Compare with `a[4] = 9` (shift). Compare with `a[3] = 5`: since `5 > 6` is false, stop — 1 shift. Insert 6 at index 4.
  Array: `[1, 2, 5, 5, 6, 9]`

Total shifts: \( 1 + 0 + 3 + 1 + 1 = 6 \).

**Check (verified by running the algorithm in Python):**

```python
def insertion_sort_count_shifts(arr):
    a = arr[:]
    total_shifts = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
            total_shifts += 1
        a[j + 1] = key
    return a, total_shifts

print(insertion_sort_count_shifts([5, 2, 9, 1, 5, 6]))
# (([1, 2, 5, 5, 6, 9], 6))
```

Running this confirms the sorted array is `[1, 2, 5, 5, 6, 9]` with exactly 6 total shifts, matching the hand trace.

**Common mistake:** Miscounting a "shift" as a full swap of two elements (which would double-count), or stopping the inner comparison loop too early/late by using `>=` instead of `>`, which would incorrectly reorder the two equal 5's or cause an extra shift.

## Answer

Total number of shifts: **6**. Sorted array: `[1, 2, 5, 5, 6, 9]`.
