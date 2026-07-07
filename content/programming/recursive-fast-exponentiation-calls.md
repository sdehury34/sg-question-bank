---
title: Number of recursive calls in fast exponentiation of 3 to the power 13
subject: programming
topic: Recursion
level: Poly / University
difficulty: Medium
description: Trace a divide-and-conquer recursive power function to find power(3, 13) and count how many recursive calls it makes in total.
date: 2026-07-07
---

## Question

Consider the following Python function:

```python
def power(base, exp):
    if exp == 0:
        return 1
    half = power(base, exp // 2)
    if exp % 2 == 0:
        return half * half
    else:
        return half * half * base
```

(a) What value does `power(3, 13)` return?

(b) How many times is `power` called in total, including the initial call?

## Solution

**Tracing the exponent argument.** Each call halves `exp` using integer division, so the sequence of exponents across the recursion is:

$$13 \rightarrow 6 \rightarrow 3 \rightarrow 1 \rightarrow 0$$

That is 5 calls in total: `power(3,13)`, `power(3,6)`, `power(3,3)`, `power(3,1)`, `power(3,0)`.

**Unwinding the return values, from the base case upward:**

- `power(3, 0)` → `exp == 0`, returns **1**.
- `power(3, 1)` → `half = power(3, 0) = 1`; `exp` is odd, so returns `half * half * base = 1 * 1 * 3 = 3`.
- `power(3, 3)` → `half = power(3, 1) = 3`; `exp` is odd, so returns `half * half * base = 3 * 3 * 3 = 27`.
- `power(3, 6)` → `half = power(3, 3) = 27`; `exp` is even, so returns `half * half = 27 * 27 = 729`.
- `power(3, 13)` → `half = power(3, 6) = 729`; `exp` is odd, so returns `half * half * base = 729 * 729 * 3 = 531441 * 3 = 1594323`.

**Check.** \(3^{13} = 1594323\), which matches directly (verified by computing `3**13` in Python). This "fast exponentiation" approach uses \(O(\log(\text{exp}))\) multiplications and recursive calls, rather than the \(O(\text{exp})\) calls a naive `power(base, exp) = base * power(base, exp-1)` recursion would need.

**Common mistake:** assuming this recursion behaves like the naive `exp - 1` version and expecting 13 (or 14) calls. Because `exp` is halved rather than decremented, the number of calls grows with \(\log_2(\text{exp})\), not with `exp` itself — here \(\lfloor \log_2 13 \rfloor + 1 = 4\) halvings down to 0, i.e. 5 calls, not 13.

## Answer

(a) `power(3, 13)` returns **1594323**.

(b) `power` is called **5** times in total.
