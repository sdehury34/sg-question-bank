---
title: Solving 2^(2x+1) − 9(2^x) + 4 = 0 using substitution
subject: amath
topic: Indices, Surds and Exponential Equations
level: O-Level
difficulty: Medium
description: Solve the exponential equation 2^(2x+1) − 9(2^x) + 4 = 0 by substituting y = 2^x to form a quadratic.
date: 2026-07-18
---

## Question

Solve the equation

$$2^{2x+1} - 9(2^{x}) + 4 = 0$$

giving your answer(s) for \(x\) exactly.

## Solution

**Rewrite in terms of a single power of 2.** Note that

$$2^{2x+1} = 2 \cdot 2^{2x} = 2 \cdot (2^{x})^{2}$$

Let \(y = 2^{x}\) (so \(y > 0\)). The equation becomes

$$2y^{2} - 9y + 4 = 0$$

**Solve the quadratic.** The discriminant is \(b^2 - 4ac = (-9)^2 - 4(2)(4) = 81 - 32 = 49\), so

$$y = \frac{9 \pm \sqrt{49}}{4} = \frac{9 \pm 7}{4}$$

This gives \(y = 4\) or \(y = \tfrac{1}{2}\). Both are positive, so both are valid values of \(2^x\).

**Convert back to \(x\).**

- \(2^{x} = 4 = 2^{2} \Rightarrow x = 2\)
- \(2^{x} = \tfrac{1}{2} = 2^{-1} \Rightarrow x = -1\)

**Check by substitution.**

- At \(x = 2\): \(2^{5} - 9(2^{2}) + 4 = 32 - 36 + 4 = 0\) ✓
- At \(x = -1\): \(2^{-1} - 9(2^{-1}) + 4 = 0.5 - 4.5 + 4 = 0\) ✓

**Common mistake:** writing \(2^{2x+1}\) as \((2^{x})^{2}\) and dropping the factor of 2 out front (i.e. forgetting the "+1" in the index contributes a multiplicative 2, not just a doubling of the exponent). This gives the wrong quadratic \(y^2 - 9y + 4 = 0\) and wrong roots. Also remember to reject any root \(y \le 0\) if one arises, since \(2^x > 0\) for all real \(x\) — here both roots happen to be valid.

## Answer

\(x = 2\) or \(x = -1\).
