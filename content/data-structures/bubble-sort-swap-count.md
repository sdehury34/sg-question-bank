---
title: Counting the number of swaps in bubble sort on a 5-element array
subject: data-structures
topic: Sorting Algorithms
level: Poly / University
difficulty: Medium
description: Trace bubble sort with early-exit optimisation on [5, 1, 4, 2, 8] and count the total number of swaps performed.
date: 2026-07-13
---

## Question

Trace the bubble sort algorithm (ascending order, with the early-exit optimisation that stops as soon as a pass makes no swaps) on the array:

$$[5, 1, 4, 2, 8]$$

Show the array after each pass, and state the total number of swaps performed.

## Solution

**Algorithm.** Each pass compares adjacent elements left to right, swapping any pair that is out of order. If a full pass completes with zero swaps, the array is already sorted and the algorithm stops early.

**Pass 1** — compare (5,1),(5,4),(5,2),(4,8) as the window shifts right:

- 5 > 1 → swap → [1, 5, 4, 2, 8]
- 5 > 4 → swap → [1, 4, 5, 2, 8]
- 5 > 2 → swap → [1, 4, 2, 5, 8]
- 5 < 8 → no swap → [1, 4, 2, 5, 8]

After pass 1: **[1, 4, 2, 5, 8]** — 3 swaps. (The last element, 8, is now guaranteed in its final position, so pass 2 only needs to check the first 4 elements.)

**Pass 2** — compare (1,4),(4,2),(2,5):

- 1 < 4 → no swap
- 4 > 2 → swap → [1, 2, 4, 5, 8]
- 4 < 5 → no swap

After pass 2: **[1, 2, 4, 5, 8]** — 1 swap.

**Pass 3** — compare (1,2),(2,4):

- 1 < 2 → no swap
- 2 < 4 → no swap

After pass 3: **[1, 2, 4, 5, 8]** — 0 swaps → early exit, array is sorted.

**Total swaps: \(3 + 1 + 0 = 4\).**

**Check.** The final array [1, 2, 4, 5, 8] contains the same 5 elements as the input in ascending order, confirming a correct sort. Running the standard bubble sort algorithm on [5, 1, 4, 2, 8] independently also yields exactly 4 swaps across 2 productive passes before the confirming zero-swap pass.

**Common mistake:** counting *comparisons* instead of *swaps* (there are 4 + 3 + 2 = 9 comparisons across the three passes, but only 4 of them result in an actual swap), or forgetting that the early-exit pass (pass 3) still counts as a pass even though it performs no swaps.

## Answer

Total swaps = **4**. Sorted array: [1, 2, 4, 5, 8].
