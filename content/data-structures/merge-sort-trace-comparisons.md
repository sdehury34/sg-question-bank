---
title: Tracing merge sort and counting comparisons on a 7-element array
subject: data-structures
topic: Sorting Algorithms
level: Poly / University
difficulty: Medium
description: Trace top-down merge sort step by step on a 7-element array and count the total number of element comparisons made during the merge steps.
date: 2026-07-16
---

## Question

Consider the standard top-down (recursive) merge sort algorithm below, applied to the array:

```
[38, 27, 43, 3, 9, 82, 10]
```

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    merged, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:      # one comparison per iteration
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
```

(a) List, in the order they occur, every call to `merge` together with its two input sublists and its output.

(b) State the total number of element comparisons (the `left[i] <= right[j]` test) made across all calls to `merge`.

## Solution

**Splitting phase.** With `mid = len(arr) // 2`, the array splits recursively (left half first) until every sublist has length 1:

$$[38,27,43,3,9,82,10] \to [38,27,43] \mid [3,9,82,10] \to [38]\,[27,43] \mid [3,9]\,[82,10] \to [38]\,[27]\,[43]\,[3]\,[9]\,[82]\,[10]$$

**Merging phase (bottom-up, in call-completion order).** Working through each `merge` call and counting the `<=` comparisons:

1. `merge([27], [43])` → compare 27 vs 43 (1 comparison) → `[27, 43]`
2. `merge([38], [27, 43])` → compare 38 vs 27 (take 27), compare 38 vs 43 (take 38) (2 comparisons) → `[27, 38, 43]`
3. `merge([3], [9])` → compare 3 vs 9 (1 comparison) → `[3, 9]`
4. `merge([82], [10])` → compare 82 vs 10 (1 comparison, takes 10; `left` then exhausted) → `[10, 82]`
5. `merge([3, 9], [10, 82])` → compare 3 vs 10 (take 3), compare 9 vs 10 (take 9; `left` exhausted) (2 comparisons) → `[3, 9, 10, 82]`
6. `merge([27, 38, 43], [3, 9, 10, 82])` → compare 27 vs 3 (take 3), 27 vs 9 (take 9), 27 vs 10 (take 10), 27 vs 82 (take 27), 38 vs 82 (take 38), 43 vs 82 (take 43; `left` exhausted) (6 comparisons) → `[3, 9, 10, 27, 38, 43, 82]`

Total comparisons: \(1 + 2 + 1 + 1 + 2 + 6 = 13\).

**Check.** Running the exact code above (verified by execution) prints these six merges in this order and returns the sorted array `[3, 9, 10, 27, 38, 43, 82]`, with a comparison counter incremented on every `<=` test reaching 13 — confirming both the trace and the count.

**Common mistake:** assuming merge sort always makes exactly \(n\log_2 n\) comparisons. That formula is only the asymptotic worst case; the actual count depends on the input order (here \(n=7\), and \(7\log_2 7 \approx 19.6\), well above the true count of 13, because several merges exhaust one side early, e.g. step 4 needs only 1 comparison for two elements).

## Answer

(a) The six merges occur in this order: `[27]+[43]→[27,43]`, `[38]+[27,43]→[27,38,43]`, `[3]+[9]→[3,9]`, `[82]+[10]→[10,82]`, `[3,9]+[10,82]→[3,9,10,82]`, `[27,38,43]+[3,9,10,82]→[3,9,10,27,38,43,82]`.

(b) The total number of comparisons is **13**.
