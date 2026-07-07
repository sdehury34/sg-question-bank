---
title: Big-O analysis of a triangular nested loop and a halving loop
subject: data-structures
topic: Complexity Analysis
level: Poly / University
difficulty: Medium
description: Determine the time complexity of a nested loop where the inner loop runs i times, and of a loop whose counter halves each iteration.
date: 2026-07-01
---

## Question

State the time complexity of each function in Big-O notation, and justify your answers.

```python
def f(n):
    total = 0
    for i in range(n):
        for j in range(i):
            total += 1
    return total

def g(n):
    count = 0
    while n > 1:
        n = n // 2
        count += 1
    return count
```

## Solution

**Function `f` — triangular nested loop.** The inner loop runs `i` times for each outer value of `i`, so the total number of iterations is

$$0 + 1 + 2 + \cdots + (n-1) = \frac{n(n-1)}{2}$$

Expanding gives \(\frac{1}{2}n^2 - \frac{1}{2}n\). In Big-O we keep the dominant term and drop constants, so

$$f(n) \in O(n^2)$$

**Key point:** the inner loop depending on `i` does **not** make it \(O(n \log n)\) — the arithmetic series still sums to a quadratic.

**Function `g` — halving loop.** Each iteration divides `n` by 2. Starting from \(n\), the loop runs until the value reaches 1, which takes about \(\log_2 n\) iterations (e.g. \(n = 64\): 64 → 32 → 16 → 8 → 4 → 2 → 1 is 6 steps, and \(\log_2 64 = 6\)). So

$$g(n) \in O(\log n)$$

**Rule of thumb:** loops that *count up or down by a constant* contribute a factor of \(n\); loops that *multiply or divide the counter by a constant* contribute a factor of \(\log n\).

## Answer

- `f(n)` is \(O(n^2)\) — the iterations form an arithmetic series summing to \(\frac{n(n-1)}{2}\).
- `g(n)` is \(O(\log n)\) — the value of `n` halves each iteration.
