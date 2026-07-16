---
title: Finding unknown coefficients in a cubic using the factor and remainder theorems
subject: amath
topic: Factor Theorem
level: O-Level
difficulty: Medium
description: Use the factor theorem and remainder theorem to find unknown coefficients in a cubic polynomial, then factorise it completely.
date: 2026-07-17
---

## Question

It is given that \(f(x) = 2x^3 + ax^2 + bx - 3\), where \(a\) and \(b\) are constants.

\((x - 1)\) is a factor of \(f(x)\). When \(f(x)\) is divided by \((x + 1)\), the remainder is \(-8\).

(a) Find the values of \(a\) and \(b\).

(b) Hence factorise \(f(x)\) completely.

## Solution

**Step 1 — Apply the factor theorem.**

Since \((x - 1)\) is a factor, \(f(1) = 0\):

$$f(1) = 2(1)^3 + a(1)^2 + b(1) - 3 = 2 + a + b - 3 = a + b - 1$$

$$a + b - 1 = 0 \quad\Rightarrow\quad a + b = 1 \quad \text{...(1)}$$

**Step 2 — Apply the remainder theorem.**

Dividing by \((x + 1)\) leaves remainder \(-8\), so \(f(-1) = -8\):

$$f(-1) = 2(-1)^3 + a(-1)^2 + b(-1) - 3 = -2 + a - b - 3 = a - b - 5$$

$$a - b - 5 = -8 \quad\Rightarrow\quad a - b = -3 \quad \text{...(2)}$$

**Step 3 — Solve (1) and (2) simultaneously.**

Adding (1) and (2): \(2a = -2 \Rightarrow a = -1\).

Substituting into (1): \(-1 + b = 1 \Rightarrow b = 2\).

**Check:** with \(a = -1, b = 2\), \(f(x) = 2x^3 - x^2 + 2x - 3\).
\(f(1) = 2 - 1 + 2 - 3 = 0\) ✓. \(f(-1) = -2 - 1 - 2 - 3 = -8\) ✓.

**Step 4 — Divide \(f(x)\) by \((x - 1)\) to factorise completely.**

$$2x^3 - x^2 + 2x - 3 = (x - 1)(2x^2 + x + 3)$$

by long division: \(2x^3 - x^2 + 2x - 3 - (2x^3 - 2x^2) = x^2 + 2x - 3\); \(x^2 + 2x - 3 - (x^2 - x) = 3x - 3\); \(3x - 3 - (3x - 3) = 0\), giving quotient \(2x^2 + x + 3\) with zero remainder.

The discriminant of \(2x^2 + x + 3\) is \(1^2 - 4(2)(3) = -23 < 0\), so it has no further real linear factors.

**Common mistake:** dropping the sign when substituting a negative value into an odd power, e.g. writing \((-1)^3 = 1\) instead of \(-1\) — this flips the sign of the whole equation in Step 2.

## Answer

(a) \(a = -1\), \(b = 2\).

(b) \(f(x) = (x - 1)(2x^2 + x + 3)\).
