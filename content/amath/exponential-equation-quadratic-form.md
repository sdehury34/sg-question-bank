---
title: Solving 4^x − 5(2^x) + 4 = 0 as a hidden quadratic equation
subject: amath
topic: Exponential Equations
level: O-Level
difficulty: Medium
description: Solve the exponential equation 4^x − 5(2^x) + 4 = 0 by substituting y = 2^x to form a quadratic.
date: 2026-07-08
---

## Question

Solve the equation \(4^x - 5(2^x) + 4 = 0\) for \(x\).

## Solution

**Step 1 — Rewrite \(4^x\) in terms of \(2^x\).**

Since \(4^x = (2^2)^x = (2^x)^2\), let \(y = 2^x\). The equation becomes

$$y^2 - 5y + 4 = 0$$

**Step 2 — Factorise and solve for \(y\).**

$$(y - 1)(y - 4) = 0 \quad\Rightarrow\quad y = 1 \text{ or } y = 4$$

**Step 3 — Convert back to \(x\).**

Case \(y = 1\): \(2^x = 1 = 2^0 \Rightarrow x = 0\).

Case \(y = 4\): \(2^x = 4 = 2^2 \Rightarrow x = 2\).

**Step 4 — Check both roots in the original equation.**

At \(x = 0\): \(4^0 - 5(2^0) + 4 = 1 - 5 + 4 = 0\). ✓

At \(x = 2\): \(4^2 - 5(2^2) + 4 = 16 - 20 + 4 = 0\). ✓

**Common mistake:** solving the quadratic \(y^2 - 5y + 4 = 0\) and stopping at \(y = 1\) or \(y = 4\), forgetting to convert back to \(x\) — the question asks for \(x\), not \(y\). Another common slip is writing \(4^x = 2 \cdot 2^x\) instead of \((2^x)^2\).

## Answer

\(x = 0\) or \(x = 2\).
