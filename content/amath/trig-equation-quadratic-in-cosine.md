---
title: Solving 2sin²x − cos x − 1 = 0 for 0° ≤ x ≤ 360°
subject: amath
topic: Trigonometric Equations
level: O-Level
difficulty: Medium
description: Solve the trigonometric equation 2sin²x − cos x − 1 = 0 for 0° to 360° by converting it into a quadratic in cos x.
date: 2026-07-24
---

## Question

Solve, for \(0° \le x \le 360°\), the equation

$$2\sin^2 x - \cos x - 1 = 0$$

## Solution

**Step 1 — Convert to a single trig ratio.** Use the identity \(\sin^2 x = 1 - \cos^2 x\):

$$2(1 - \cos^2 x) - \cos x - 1 = 0$$

$$2 - 2\cos^2 x - \cos x - 1 = 0$$

$$-2\cos^2 x - \cos x + 1 = 0$$

Multiply through by \(-1\) so the leading coefficient is positive:

$$2\cos^2 x + \cos x - 1 = 0$$

**Step 2 — Factorise as a quadratic in \(\cos x\).** Let \(c = \cos x\):

$$2c^2 + c - 1 = 0 \implies (2c - 1)(c + 1) = 0$$

so \(\cos x = \dfrac{1}{2}\) or \(\cos x = -1\).

**Step 3 — Solve each case on \(0° \le x \le 360°\).**

For \(\cos x = \dfrac{1}{2}\): the basic angle is \(60°\). Cosine is positive in the 1st and 4th quadrants, giving

$$x = 60° \quad \text{or} \quad x = 360° - 60° = 300°$$

For \(\cos x = -1\): this is the boundary value attained only once per revolution, at

$$x = 180°$$

**Step 4 — Check each root in the original equation.**

- \(x = 60°\): \(2(\tfrac{\sqrt3}{2})^2 - \tfrac12 - 1 = 2(\tfrac34) - \tfrac12 - 1 = 1.5 - 1.5 = 0\) ✓
- \(x = 180°\): \(2(0)^2 - (-1) - 1 = 0 + 1 - 1 = 0\) ✓
- \(x = 300°\): \(2(-\tfrac{\sqrt3}{2})^2 - \tfrac12 - 1 = 1.5 - 1.5 = 0\) ✓

All three roots satisfy the equation.

**Common mistake:** when dividing/multiplying the equation \(-2\cos^2x - \cos x + 1 = 0\) by \(-1\), students often flip the sign of only some terms, e.g. writing \(2\cos^2x - \cos x - 1 = 0\) instead of \(2\cos^2x + \cos x - 1 = 0\). It's also common to find \(x = 60°\) but forget the second quadrant solution \(x = 300°\), or to mistakenly treat \(\cos x = -1\) as having two solutions in the range (it only has one, since \(x=180°\) is a boundary/turning point, not a quadrant pair).

## Answer

$$x = 60°, \ 180°, \ 300°$$
