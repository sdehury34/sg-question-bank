---
title: Partial fractions of (5x − 4)/((x − 2)(x + 1))
subject: amath
topic: Partial Fractions
level: O-Level
difficulty: Easy
description: Express (5x − 4)/((x − 2)(x + 1)) in partial fractions using the cover-up method for distinct linear factors.
date: 2026-07-09
---

## Question

Express \(\dfrac{5x - 4}{(x - 2)(x + 1)}\) in partial fractions.

## Solution

**Step 1 — Set up the partial fraction form.** Since the denominator has two distinct linear factors,

$$\frac{5x - 4}{(x - 2)(x + 1)} = \frac{A}{x - 2} + \frac{B}{x + 1}$$

**Step 2 — Clear the denominators** by multiplying both sides by \((x-2)(x+1)\):

$$5x - 4 = A(x + 1) + B(x - 2)$$

**Step 3 — Substitute convenient values of \(x\)** to isolate each constant.

Let \(x = 2\): \(5(2) - 4 = A(2 + 1) \Rightarrow 6 = 3A \Rightarrow A = 2\)

Let \(x = -1\): \(5(-1) - 4 = B(-1 - 2) \Rightarrow -9 = -3B \Rightarrow B = 3\)

**Step 4 — Write the result.**

$$\frac{5x - 4}{(x - 2)(x + 1)} = \frac{2}{x - 2} + \frac{3}{x + 1}$$

**Check:** combine the right-hand side back over a common denominator:

$$\frac{2(x+1) + 3(x-2)}{(x-2)(x+1)} = \frac{2x + 2 + 3x - 6}{(x-2)(x+1)} = \frac{5x - 4}{(x-2)(x+1)} \checkmark$$

This matches the original expression, confirming \(A = 2\) and \(B = 3\).

**Common mistake:** substituting the wrong root into the wrong factor — e.g. using \(x = 2\) to try to isolate \(B\). Always substitute the value that makes one bracket vanish, so only the constant attached to the *other* bracket survives.

## Answer

$$\frac{5x - 4}{(x - 2)(x + 1)} = \frac{2}{x - 2} + \frac{3}{x + 1}$$
