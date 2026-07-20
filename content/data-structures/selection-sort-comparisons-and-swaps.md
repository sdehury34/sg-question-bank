---
title: Counting comparisons and swaps when selection-sorting [29, 10, 14, 37, 13]
subject: data-structures
topic: Sorting Algorithms
level: Poly / University
difficulty: Medium
description: Trace selection sort on the array [29, 10, 14, 37, 13] pass by pass and count the total comparisons and swaps performed.
date: 2026-07-21
---

## Question

Trace selection sort (ascending order) on the array

```
[29, 10, 14, 37, 13]
```

Show the array after each pass, and state the total number of comparisons and the total number of swaps performed. Use the convention that in each pass, the algorithm scans the unsorted portion to find the minimum, and performs a swap **only if** that minimum is not already at the front of the unsorted portion.

## Solution

**Algorithm.** For each index \(i\) from \(0\) to \(n-2\), scan positions \(i+1 \dots n-1\) to find the index of the minimum value, comparing it against the running minimum each time (that comparison counts even if it doesn't change the minimum). Then swap the minimum into position \(i\), unless it is already there.

**Pass 1 (i = 0), array `[29, 10, 14, 37, 13]`:**
Compare positions 1,2,3,4 against the running minimum: \(10 < 29\) (min→10), \(14 < 10\)? no, \(37 < 10\)? no, \(13 < 10\)? no. → 4 comparisons. Minimum is \(10\) at index 1, swap with index 0.
Array: `[10, 29, 14, 37, 13]`

**Pass 2 (i = 1), unsorted part `[29, 14, 37, 13]`:**
Compare positions 2,3,4: \(14 < 29\) (min→14), \(37 < 14\)? no, \(13 < 14\)? yes (min→13). → 3 comparisons. Minimum is \(13\) at index 4, swap with index 1.
Array: `[10, 13, 14, 37, 29]`

**Pass 3 (i = 2), unsorted part `[14, 37, 29]`:**
Compare positions 3,4: \(37 < 14\)? no, \(29 < 14\)? no. → 2 comparisons. Minimum is already \(14\) at index 2 — **no swap**.
Array: `[10, 13, 14, 37, 29]`

**Pass 4 (i = 3), unsorted part `[37, 29]`:**
Compare position 4: \(29 < 37\)? yes (min→29). → 1 comparison. Minimum is \(29\) at index 4, swap with index 3.
Array: `[10, 13, 14, 29, 37]`

**Totals:** comparisons \(= 4+3+2+1 = 10\); swaps \(= 3\) (passes 1, 2, and 4 swapped; pass 3 did not).

**Check.** For selection sort on \(n\) elements, the number of comparisons is always \(\binom{n}{2} = \frac{n(n-1)}{2}\) regardless of the input, since every pass scans the full remaining unsorted portion. For \(n=5\): \(\frac{5 \times 4}{2} = 10\), matching the count above. This was also confirmed by running the algorithm in Python, which reproduces the same trace, 10 comparisons, and 3 swaps.

**Common mistake:** assuming the number of swaps always equals \(n - 1\) (one per pass). Selection sort skips the swap whenever the current minimum is already in the correct position — as happened in pass 3 here — so the swap count can be less than \(n-1\), while the comparison count is always fixed at \(n(n-1)/2\).

## Answer

Final sorted array: **`[10, 13, 14, 29, 37]`**
Total comparisons: **10**
Total swaps: **3**
