---
title: Tracing bubble sort passes and counting swaps on a small list
subject: programming
topic: Sorting Algorithms
level: Poly / University
difficulty: Medium
description: Trace bubble sort pass by pass on a 5-element list, counting swaps per pass until the list is sorted.
date: 2026-07-17
---

## Question

Consider this bubble sort implementation, which stops early once a full pass makes no swaps:

```python
def bubble_sort(arr):
    n = len(arr)
    for p in range(n - 1):
        swapped = False
        for i in range(n - 1 - p):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
    return arr
```

Trace `bubble_sort([5, 1, 4, 2, 8])` pass by pass. For each pass, state the resulting list and the number of swaps made. How many passes run before the function returns, and what is the final sorted list?

## Solution

**Step 1 — Pass 1** (compare index 0 to 3, i.e. `i` in `range(4)`).

| Comparison | Action |
|---|---|
| 5, 1 | swap → [1, 5, 4, 2, 8] |
| 5, 4 | swap → [1, 4, 5, 2, 8] |
| 5, 2 | swap → [1, 4, 2, 5, 8] |
| 5, 8 | no swap |

End of pass 1: **[1, 4, 2, 5, 8]**, 3 swaps. `swapped = True`, so the outer loop continues.

**Step 2 — Pass 2** (`i` in `range(3)`).

| Comparison | Action |
|---|---|
| 1, 4 | no swap |
| 4, 2 | swap → [1, 2, 4, 5, 8] |
| 4, 5 | no swap |

End of pass 2: **[1, 2, 4, 5, 8]**, 1 swap. `swapped = True`, so the outer loop continues.

**Step 3 — Pass 3** (`i` in `range(2)`).

| Comparison | Action |
|---|---|
| 1, 2 | no swap |
| 2, 4 | no swap |

End of pass 3: **[1, 2, 4, 5, 8]**, 0 swaps. `swapped` stays `False`, so `break` fires and the function returns.

**Verification:** running this exact code confirms the trace —

```python
>>> bubble_sort([5, 1, 4, 2, 8])
[1, 2, 4, 5, 8]
```

with pass swap counts 3, 1, 0, matching the table above.

**Common mistake:** assuming bubble sort always runs `n - 1` passes regardless of the data — the early-exit `if not swapped: break` means a nearly-sorted list can finish in fewer passes, as it does here (3 passes instead of the worst-case 4 for a 5-element list).

## Answer

The function runs **3 passes** before returning, with 3, 1, and 0 swaps respectively. The final sorted list is **[1, 2, 4, 5, 8]**.
