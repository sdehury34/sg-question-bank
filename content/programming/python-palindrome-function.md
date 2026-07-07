---
title: Writing a palindrome checker that ignores case and punctuation
subject: programming
topic: Python Basics
level: Poly / University
difficulty: Medium
description: Write a Python function is_palindrome(s) that returns True if a string reads the same forwards and backwards, ignoring case and non-alphanumeric characters.
date: 2026-07-02
---

## Question

Write a Python function `is_palindrome(s)` that returns `True` if the string `s` reads the same forwards and backwards, ignoring letter case and any characters that are not letters or digits.

For example:

```python
is_palindrome("Madam, I'm Adam")   # True
is_palindrome("race a car")        # False
is_palindrome("No lemon, no melon") # True
```

## Solution

**Step 1 — Normalise the string.** Keep only alphanumeric characters and convert to lowercase. `str.isalnum()` and a list comprehension handle this cleanly:

```python
cleaned = [c.lower() for c in s if c.isalnum()]
```

For `"Madam, I'm Adam"` this produces `['m','a','d','a','m','i','m','a','d','a','m']`.

**Step 2 — Compare with its reverse.** A list reversed with slicing is `cleaned[::-1]`. The string is a palindrome exactly when the two are equal:

```python
def is_palindrome(s):
    cleaned = [c.lower() for c in s if c.isalnum()]
    return cleaned == cleaned[::-1]
```

**Why this works:** filtering first means punctuation and spaces can never break the comparison, and lowering the case makes `M` equal to `m`.

**Complexity:** the function runs in \(O(n)\) time and uses \(O(n)\) extra space for the cleaned list. An interview follow-up is the two-pointer version, which uses \(O(1)\) extra space:

```python
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1
    return True
```

## Answer

```python
def is_palindrome(s):
    cleaned = [c.lower() for c in s if c.isalnum()]
    return cleaned == cleaned[::-1]
```
