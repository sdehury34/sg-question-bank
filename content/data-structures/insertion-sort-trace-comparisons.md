---
title: Tracing insertion sort on [8, 3, 5, 1, 9, 2] and counting comparisons
subject: data-structures
topic: Sorting Algorithms
level: Poly / University
difficulty: Medium
description: Trace insertion sort step by step on a 6-element array, showing the array after every pass and the total number of comparisons made.
date: 2026-07-24
---

## Question

Trace the **insertion sort** algorithm on the array

```
[8, 3, 5, 1, 9, 2]
```

Show the state of the array after each pass (i.e. after each new element has been inserted into the sorted prefix), and state the total number of element comparisons made during the whole sort.

## Solution

**Algorithm.** For each index \(i\) from 1 to \(n-1\), take `key = arr[i]` and shift it leftward past every element in the sorted prefix `arr[0..i-1]` that is strictly greater than `key`, comparing one adjacent pair at a time and stopping as soon as a comparison fails (or the start of the array is reached).

**Pass-by-pass trace** (starting array `[8, 3, 5, 1, 9, 2]`):

| Pass | key | Comparisons made | Array after pass |
|---|---|---|---|
| \(i=1\) | 3 | compare with 8 (8 > 3, shift) → 1 comparison | `[3, 8, 5, 1, 9, 2]` |
| \(i=2\) | 5 | compare with 8 (shift), then 3 (3 > 5? no, stop) → 2 comparisons | `[3, 5, 8, 1, 9, 2]` |
| \(i=3\) | 1 | compare with 8 (shift), 5 (shift), 3 (shift), reach start → 3 comparisons | `[1, 3, 5, 8, 9, 2]` |
| \(i=4\) | 9 | compare with 8 (8 > 9? no, stop) → 1 comparison | `[1, 3, 5, 8, 9, 2]` |
| \(i=5\) | 2 | compare with 9 (shift), 8 (shift), 5 (shift), 3 (shift), 1 (1 > 2? no, stop) → 5 comparisons | `[1, 2, 3, 5, 8, 9]` |

Total comparisons: \(1 + 2 + 3 + 1 + 5 = 12\).

**Check by direct execution.** Running the same algorithm in code confirms both the final array and the comparison count:

```python
def insertion_sort_trace(arr):
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

print(insertion_sort_trace([8, 3, 5, 1, 9, 2]))
# ([1, 2, 3, 5, 8, 9], 12)
```

This matches the hand trace exactly: final sorted array `[1, 2, 3, 5, 8, 9]` with 12 comparisons.

**Common mistake:** forgetting to stop shifting as soon as an element that is not greater than `key` is found — continuing to compare (and count) every remaining element in the sorted prefix regardless, which inflates the comparison count. Another common slip is off-by-one errors in the "reach the start of the array" case (pass \(i=3\)), where the algorithm should stop shifting *without* an extra comparison once index \(-1\) is reached.

## Answer

Final sorted array: **[1, 2, 3, 5, 8, 9]**. Total comparisons: **12**.
