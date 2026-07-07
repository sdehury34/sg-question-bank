---
title: Maximum comparisons in binary search on 1000 elements
subject: data-structures
topic: Searching Algorithms
level: Poly / University
difficulty: Medium
description: Work out the maximum number of comparisons binary search needs on a sorted array of 1000 elements, and why the answer is 10.
date: 2026-07-01
---

## Question

A sorted array contains 1000 elements. Using binary search:

1. What is the **maximum** number of comparisons needed to determine whether a target value is in the array?
2. Explain why binary search requires the array to be sorted.

## Solution

**Part 1 — Maximum comparisons.**

Each comparison lets binary search discard half of the remaining search space. Starting from 1000 elements, the worst-case sequence of remaining sizes is:

$$1000 \rightarrow 500 \rightarrow 250 \rightarrow 125 \rightarrow 62 \rightarrow 31 \rightarrow 15 \rightarrow 7 \rightarrow 3 \rightarrow 1$$

That is 9 halvings to get down to a single element, plus the final comparison of that element — at most **10 comparisons** in total.

The general formula for the worst case is

$$\lfloor \log_2 n \rfloor + 1$$

For \(n = 1000\): since \(2^9 = 512 \le 1000 \lt 1024 = 2^{10}\), we get \(\lfloor \log_2 1000 \rfloor + 1 = 9 + 1 = 10\).

**Intuition:** 10 comparisons can distinguish up to \(2^{10} = 1024\) elements, which covers 1000; 9 comparisons cover only \(2^9 = 512\), which does not.

**Part 2 — Why sorted?**

Binary search compares the target with the middle element and uses the ordering to decide which half **cannot** contain the target. If the array is unsorted, that deduction is invalid — the target could be on either side — so no half can be safely discarded, and the algorithm may return a wrong result or miss the element entirely. On unsorted data you must use linear search, which is \(O(n)\) rather than \(O(\log n)\).

## Answer

1. Maximum comparisons = **10** (from \(\lfloor \log_2 1000 \rfloor + 1\)).
2. Binary search discards half the array based on order; without sorting, the discarded half could contain the target.
