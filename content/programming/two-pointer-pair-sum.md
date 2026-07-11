---
title: Finding a pair that sums to a target using the two-pointer technique
subject: programming
topic: Two Pointers
level: Poly / University
difficulty: Medium
description: Trace the two-pointer technique on a sorted array to find a pair of numbers that sum to a target, with working Python code and verified output.
date: 2026-07-12
---

## Question

Given the **sorted** array `arr = [1, 4, 6, 8, 11, 15]` and `target = 14`, use the two-pointer technique (one pointer starting at each end of the array) to find a pair of elements that sum to `target`. Trace the position of both pointers and the sum at each step, then write a Python function that implements this and confirm the result.

## Solution

Start with `left = 0` (value 1) and `right = 5` (value 15). At each step, compare the sum of the two pointed-to values with the target: if the sum is too small, move `left` right (to increase the sum); if too large, move `right` left (to decrease the sum); if equal, a pair is found.

| Step | left (value) | right (value) | sum | action |
|---|---|---|---|---|
| 1 | 0 (1) | 5 (15) | 16 | 16 > 14 → move right left |
| 2 | 0 (1) | 4 (11) | 12 | 12 < 14 → move left right |
| 3 | 1 (4) | 4 (11) | 15 | 15 > 14 → move right left |
| 4 | 1 (4) | 3 (8) | 12 | 12 < 14 → move left right |
| 5 | 2 (6) | 3 (8) | 14 | 14 == 14 → **found** |

Since the array is sorted, each move discards exactly one value that provably cannot be part of a valid pair with the current partner, so the whole array is scanned in \( O(n) \) time using \( O(1) \) extra space — better than the \( O(n^2) \) brute-force check of every pair.

```python
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return (arr[left], arr[right])
        elif s < target:
            left += 1
        else:
            right -= 1
    return None

print(two_sum_sorted([1, 4, 6, 8, 11, 15], 14))
```

Running this prints `(6, 8)`, matching the hand trace above.

**Common mistake:** Applying the two-pointer technique to an *unsorted* array — the "move the pointer that reduces/increases the sum" logic only works because the array is sorted; on unsorted input it can skip over valid pairs.

## Answer

The pair is **(6, 8)**, found after 5 steps.
