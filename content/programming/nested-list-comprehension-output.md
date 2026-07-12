---
title: Predicting the output of a nested Python list comprehension with a filter
subject: programming
topic: List Comprehensions
level: Poly / University
difficulty: Easy
description: Predict the output of a nested list comprehension that iterates over a matrix and filters for even values.
date: 2026-07-13
---

## Question

What does the following Python code print?

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = [row[i] for row in matrix for i in range(len(row)) if row[i] % 2 == 0]
print(result)
```

## Solution

**Step 1 — Understand the comprehension's loop order.** A comprehension with two `for` clauses nests them in the order written, so this is equivalent to:

```python
result = []
for row in matrix:
    for i in range(len(row)):
        if row[i] % 2 == 0:
            result.append(row[i])
```

**Step 2 — Walk through each row.**

- `row = [1, 2, 3]`: indices 0,1,2 → values 1, 2, 3 → only `2` is even → append 2
- `row = [4, 5, 6]`: values 4, 5, 6 → `4` and `6` are even → append 4, append 6
- `row = [7, 8, 9]`: values 7, 8, 9 → only `8` is even → append 8

**Step 3 — Combine in order.**

$$\text{result} = [2, 4, 6, 8]$$

**Verification (ran the exact code):**

```
>>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> result = [row[i] for row in matrix for i in range(len(row)) if row[i] % 2 == 0]
>>> print(result)
[2, 4, 6, 8]
```

**Common mistake:** assuming the comprehension collects an even number from *each* row (one per row), giving a wrong prediction like `[2, 4, 8]`. In fact each row can contribute zero, one, or more values — row `[4, 5, 6]` contributes two even numbers (4 and 6), which is easy to miss when reading the comprehension too quickly.

## Answer

```
[2, 4, 6, 8]
```
