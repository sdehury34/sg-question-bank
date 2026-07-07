---
title: Term independent of x in the expansion of (2x − 1/x²)⁹
subject: amath
topic: Binomial Theorem
level: O-Level
difficulty: Medium
description: Find the term independent of x in the binomial expansion of (2x − 1/x²)⁹ using the general term.
date: 2026-07-06
---

## Question

Find the term independent of \(x\) in the expansion of \(\left(2x - \dfrac{1}{x^2}\right)^9\).

## Solution

**Step 1 — Write the general term.**

$$T_{r+1} = \binom{9}{r} (2x)^{9-r} \left(-\frac{1}{x^2}\right)^r$$

**Step 2 — Collect the powers of \(x\).**

$$T_{r+1} = \binom{9}{r} \, 2^{9-r} \,(-1)^r \, x^{9-r} \cdot x^{-2r} = \binom{9}{r} \, 2^{9-r} \,(-1)^r \, x^{9-3r}$$

**Step 3 — Set the power of \(x\) to zero** (term independent of \(x\)):

$$9 - 3r = 0 \quad\Rightarrow\quad r = 3$$

**Step 4 — Substitute \(r = 3\).**

$$T_4 = \binom{9}{3} \, 2^{6} \, (-1)^3 = 84 \times 64 \times (-1) = -5376$$

**Common mistake:** forgetting the \((-1)^r\) from the negative sign inside the bracket, which gives the wrong sign for the final term.

## Answer

The term independent of \(x\) is **−5376**.
