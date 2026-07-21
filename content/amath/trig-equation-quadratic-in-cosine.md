---
title: Solving 2 sin²x − cos x = 1 for 0° ≤ x ≤ 360°
subject: amath
topic: Trigonometric Equations
level: O-Level
difficulty: Medium
description: Solve the trigonometric equation 2 sin²x − cos x = 1 for 0° ≤ x ≤ 360° by reducing it to a quadratic in cos x.
date: 2026-07-22
---

## Question

Solve, for \(0° \le x \le 360°\), the equation

$$2\sin^2 x - \cos x = 1$$

giving all solutions.

## Solution

**Step 1 — Reduce to a single trig ratio.** Use the identity \(\sin^2 x = 1 - \cos^2 x\) to rewrite everything in terms of \(\cos x\):

$$2(1 - \cos^2 x) - \cos x = 1$$

$$2 - 2\cos^2 x - \cos x = 1$$

$$2\cos^2 x + \cos x - 1 = 0$$

**Step 2 — Factorise as a quadratic.** Let \(c = \cos x\):

$$2c^2 + c - 1 = 0 \implies (2c - 1)(c + 1) = 0$$

$$c = \frac{1}{2} \quad \text{or} \quad c = -1$$

**Step 3 — Solve each case for \(0° \le x \le 360°\).**

- \(\cos x = \frac{1}{2}\): the basic angle is \(60°\). Cosine is positive in the 1st and 4th quadrants, so \(x = 60°\) or \(x = 360° - 60° = 300°\).
- \(\cos x = -1\): this occurs only at \(x = 180°\).

**Step 4 — Check each solution in the original equation.**

- \(x = 60°\): \(2\sin^2 60° - \cos 60° = 2\left(\frac{\sqrt3}{2}\right)^2 - \frac12 = 2\left(\frac34\right) - \frac12 = 1.5 - 0.5 = 1\) ✓
- \(x = 180°\): \(2\sin^2 180° - \cos 180° = 2(0) - (-1) = 1\) ✓
- \(x = 300°\): \(2\sin^2 300° - \cos 300° = 2\left(\frac{\sqrt3}{2}\right)^2 - \frac12 = 1.5 - 0.5 = 1\) ✓

All three solutions check out.

**Common mistake:** applying the identity incorrectly as \(\sin^2 x = 1 - \cos x\) (confusing it with \(1 - \cos^2 x\)), which turns the equation into a linear one in \(\cos x\) and loses the second pair of solutions at \(x = 60°\) and \(300°\).

## Answer

$$x = 60°, \ 180°, \ 300°$$
