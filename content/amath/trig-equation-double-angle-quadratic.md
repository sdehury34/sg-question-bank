---
title: Solving 2cos²θ − sinθ − 1 = 0 for 0° ≤ θ ≤ 360°
subject: amath
topic: Trigonometric Equations
level: O-Level
difficulty: Medium
description: Solve the trigonometric equation 2cos²θ − sinθ − 1 = 0 for 0° to 360° by converting it into a quadratic in sinθ.
date: 2026-07-13
---

## Question

Solve the equation \(2\cos^2\theta - \sin\theta - 1 = 0\) for \(0^\circ \le \theta \le 360^\circ\).

## Solution

**Step 1 — Convert to a single trig ratio.** Use \(\cos^2\theta = 1 - \sin^2\theta\):

$$2(1 - \sin^2\theta) - \sin\theta - 1 = 0$$

$$2 - 2\sin^2\theta - \sin\theta - 1 = 0$$

$$-2\sin^2\theta - \sin\theta + 1 = 0$$

Multiply through by \(-1\):

$$2\sin^2\theta + \sin\theta - 1 = 0$$

**Step 2 — Factorise as a quadratic in \(\sin\theta\).**

$$(2\sin\theta - 1)(\sin\theta + 1) = 0$$

So \(\sin\theta = \dfrac{1}{2}\) or \(\sin\theta = -1\).

**Step 3 — Solve each case in the given range.**

For \(\sin\theta = \dfrac{1}{2}\): basic angle \(= 30^\circ\). Since sine is positive in the 1st and 2nd quadrants:

$$\theta = 30^\circ, \ 180^\circ - 30^\circ = 150^\circ$$

For \(\sin\theta = -1\): this occurs only once in \([0^\circ, 360^\circ]\):

$$\theta = 270^\circ$$

**Step 4 — Check each root in the original equation.**

- \(\theta = 30^\circ\): \(2\cos^2 30^\circ - \sin 30^\circ - 1 = 2(0.75) - 0.5 - 1 = 0\) ✓
- \(\theta = 150^\circ\): \(2\cos^2 150^\circ - \sin 150^\circ - 1 = 2(0.75) - 0.5 - 1 = 0\) ✓
- \(\theta = 270^\circ\): \(2\cos^2 270^\circ - \sin 270^\circ - 1 = 2(0) - (-1) - 1 = 0\) ✓

All three roots satisfy the equation.

**Common mistake:** treating \(\sin\theta = -1\) the same way as \(\sin\theta = \tfrac12\) and writing two solutions for it (e.g. \(270^\circ\) and \(360^\circ - 270^\circ\)). Since \(-1\) is the minimum value of sine, it is attained at exactly **one** point in a full revolution, not two.

## Answer

\(\theta = 30^\circ,\ 150^\circ,\ 270^\circ\)
