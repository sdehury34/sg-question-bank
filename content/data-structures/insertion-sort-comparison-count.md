---
title: Counting key comparisons in insertion sort on [5, 2, 4, 6, 1, 3]
subject: data-structures
topic: Sorting Algorithms
level: Poly / University
difficulty: Medium
description: Trace insertion sort on the array [5, 2, 4, 6, 1, 3] and count the total number of key comparisons performed.
date: 2026-07-09
---

## Question

Consider the standard insertion sort algorithm below, where `comparisons` is incremented every time the condition `arr[j] > key` is *evaluated* (whether it is true or false):

```
for i = 1 to n - 1:
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        comparisons += 1
        arr[j + 1] = arr[j]
        j -= 1
    if j >= 0:
        comparisons += 1        # the evaluation that stopped the loop
    arr[j + 1] = key
```

Trace this algorithm on the array \([5, 2, 4, 6, 1, 3]\) and find the total number of comparisons performed to fully sort it.

## Solution

Work through the array one insertion pass at a time. The array is 0-indexed.

**Pass \(i = 1\), key \(= 2\):** compare with \(\text{arr}[0] = 5\): \(5 > 2\), shift (1 comparison). \(j\) becomes \(-1\), loop stops (no further comparison needed since \(j < 0\)).
Array: \([2, 5, 4, 6, 1, 3]\). Comparisons so far: **1**.

**Pass \(i = 2\), key \(= 4\):** compare with \(\text{arr}[1] = 5\): \(5 > 4\), shift (1 comparison). Compare with \(\text{arr}[0] = 2\): \(2 > 4\) is false, stop (1 comparison).
Array: \([2, 4, 5, 6, 1, 3]\). Comparisons this pass: 2. Running total: **3**.

**Pass \(i = 3\), key \(= 6\):** compare with \(\text{arr}[2] = 5\): \(5 > 6\) is false, stop immediately (1 comparison).
Array unchanged: \([2, 4, 5, 6, 1, 3]\). Comparisons this pass: 1. Running total: **4**.

**Pass \(i = 4\), key \(= 1\):** compare with \(6\) (shift), \(5\) (shift), \(4\) (shift), \(2\) (shift) — all greater than 1, so all four shift, and \(j\) reaches \(-1\) (loop stops without an extra comparison).
Array: \([1, 2, 4, 5, 6, 3]\). Comparisons this pass: 4. Running total: **8**.

**Pass \(i = 5\), key \(= 3\):** compare with \(6\) (shift), \(5\) (shift), \(4\) (shift) — three shifts. Compare with \(\text{arr}[1] = 2\): \(2 > 3\) is false, stop (1 comparison).
Array: \([1, 2, 3, 4, 5, 6]\). Comparisons this pass: 4. Running total: **12**.

**Check:** this was confirmed by running the algorithm in Python, which produced the cumulative comparison counts \(1, 3, 4, 8, 12\) after each pass — matching the trace above, and the final array \([1, 2, 3, 4, 5, 6]\) is correctly sorted.

**Common mistake:** forgetting to count the final "failing" comparison that stops the `while` loop (e.g. in pass 3, students often report 0 comparisons instead of 1, because no shift happens). A comparison is counted whenever the condition is *checked*, not only when it causes a shift.

## Answer

The algorithm performs **12** key comparisons in total to sort \([5, 2, 4, 6, 1, 3]\).
