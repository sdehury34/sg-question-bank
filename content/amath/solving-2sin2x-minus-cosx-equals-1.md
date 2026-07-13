---
title: Solving 2sin²x − cos x = 1 for 0° ≤ x ≤ 360°
subject: amath
topic: Trigonometric Equations
level: O-Level
difficulty: Medium
description: Solve the trigonometric equation 2sin²x − cos x = 1 for 0° ≤ x ≤ 360° by converting to a quadratic in cos x.
date: 2026-07-14
---

## Question

Solve, for \(0° \le x \le 360°\), the equation

$$2\sin^2 x - \cos x = 1$$

giving all solutions to the nearest degree.

## Solution

**Step 1 — Convert to a single trig ratio.** Use the identity \(\sin^2 x = 1 - \cos^2 x\):

$$2(1 - \cos^2 x) - \cos x = 1$$

**Step 2 — Expand and rearrange into a quadratic in \(\cos x\).**

$$2 - 2\cos^2 x - \cos x = 1$$

$$-2\cos^2 x - \cos x + 1 = 0$$

Multiply through by \(-1\):

$$2\cos^2 x + \cos x - 1 = 0$$

**Step 3 — Factorise.** Let \(c = \cos x\):

$$2c^2 + c - 1 = 0 \quad\Rightarrow\quad (2c - 1)(c + 1) = 0$$

$$c = \frac{1}{2} \quad \text{or} \quad c = -1$$

**Step 4 — Solve each case for \(0° \le x \le 360°\).**

*Case \(\cos x = \dfrac{1}{2}\):* basic angle \(= 60°\). Cosine is positive in quadrants 1 and 4, so

$$x = 60° \quad \text{or} \quad x = 360° - 60° = 300°$$

*Case \(\cos x = -1\):*

$$x = 180°$$

**Step 5 — Check all three solutions by substitution.**

- \(x = 60°\): \(2\sin^2 60° - \cos 60° = 2(0.75) - 0.5 = 1.5 - 0.5 = 1\) ✓
- \(x = 180°\): \(2\sin^2 180° - \cos 180° = 2(0) - (-1) = 0 + 1 = 1\) ✓
- \(x = 300°\): \(2\sin^2 300° - \cos 300° = 2(0.75) - 0.5 = 1.5 - 0.5 = 1\) ✓

All three satisfy the original equation.

**Common mistake:** dividing the equation by \(\cos x\) or by a common factor at some stage, which silently discards the \(\cos x = -1\) root (\(x = 180°\)). Always solve trig equations by factorising a proper quadratic, never by cancelling a variable factor.

## Answer

$$x = 60°, \ 180°, \ 300°$$
