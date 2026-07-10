---
title: Solving simultaneous equations y = x + 1 and x² + y² = 13
subject: amath
topic: Simultaneous Equations
level: O-Level
difficulty: Medium
description: Solve a linear-quadratic simultaneous equation pair by substitution and check both solution pairs satisfy the original equations.
date: 2026-07-11
---

## Question

Solve the simultaneous equations

$$y = x + 1, \qquad x^2 + y^2 = 13$$

giving both pairs of solutions.

## Solution

**Step 1 — Substitute the linear equation into the quadratic one.** Since \(y = x+1\), replace \(y\) in the second equation:

$$x^2 + (x+1)^2 = 13$$

**Step 2 — Expand and simplify.**

$$x^2 + x^2 + 2x + 1 = 13$$

$$2x^2 + 2x - 12 = 0$$

Dividing through by 2:

$$x^2 + x - 6 = 0$$

**Step 3 — Factorise.**

$$(x+3)(x-2) = 0$$

$$x = -3 \quad \text{or} \quad x = 2$$

**Step 4 — Find the corresponding \(y\) values using \(y = x+1\).**

- \(x = -3 \Rightarrow y = -3 + 1 = -2\)
- \(x = 2 \Rightarrow y = 2 + 1 = 3\)

So the two solution pairs are \((x,y) = (-3,-2)\) and \((x,y) = (2,3)\).

**Check by substitution into \(x^2+y^2=13\):**

$$(-3)^2 + (-2)^2 = 9 + 4 = 13 \checkmark$$

$$2^2 + 3^2 = 4 + 9 = 13 \checkmark$$

Both pairs also satisfy \(y = x+1\) by construction, so both are valid.

**Common mistake:** stopping after finding only one root of the factorised quadratic (e.g. only taking \(x=2\) and discarding \(x=-3\)). Both roots of the quadratic give valid solutions unless a stated restriction (such as \(x>0\)) rules one out — always state both pairs.

## Answer

\((x,y) = (-3,-2)\) or \((x,y) = (2,3)\).
