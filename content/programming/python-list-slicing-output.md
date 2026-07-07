---
title: Predicting the output of Python list slicing
subject: programming
topic: Python Basics
level: Poly / University
difficulty: Easy
description: Trace through Python list slicing expressions including negative indices and reversed slices, and predict the printed output.
date: 2026-07-02
---

## Question

What is the output of the following Python program? Work it out by hand before running it.

```python
nums = [3, 1, 4, 1, 5, 9, 2, 6]

print(nums[2:5])
print(nums[::-1][:3])
print(nums[-3:])
```

## Solution

**Line 1 — `nums[2:5]`.** Slicing takes elements from index 2 **up to but not including** index 5. Indices 2, 3, 4 hold the values `4`, `1`, `5`:

```python
[4, 1, 5]
```

**Line 2 — `nums[::-1][:3]`.** Evaluate left to right. `nums[::-1]` reverses the list:

```python
[6, 2, 9, 5, 1, 4, 1, 3]
```

Then `[:3]` takes the first three elements of that reversed list:

```python
[6, 2, 9]
```

**Line 3 — `nums[-3:]`.** Negative indices count from the end, so `-3` is the third-last element. The slice runs from there to the end:

```python
[9, 2, 6]
```

**Key idea:** a slice `a[start:stop]` never includes `a[stop]`, and an omitted bound means "from the beginning" or "to the end".

## Answer

```python
[4, 1, 5]
[6, 2, 9]
[9, 2, 6]
```
