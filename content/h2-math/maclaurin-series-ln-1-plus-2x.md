---
title: Maclaurin series of ln(1 + 2x) up to the term in x³
subject: h2-math
topic: Maclaurin Series
level: A-Level
difficulty: Medium
description: Derive the Maclaurin expansion of ln(1 + 2x) up to the x³ term using successive differentiation, then verify it against the standard series.
date: 2026-07-14
---

## Question

Find the Maclaurin series for \(f(x) = \ln(1 + 2x)\), up to and including the term in \(x^3\).

## Solution

**Step 1 — Find the derivatives of \(f(x) = \ln(1+2x)\).**

$$f(x) = \ln(1+2x) \quad\Rightarrow\quad f(0) = \ln 1 = 0$$

$$f'(x) = \frac{2}{1+2x} \quad\Rightarrow\quad f'(0) = 2$$

$$f''(x) = \frac{-4}{(1+2x)^2} \quad\Rightarrow\quad f''(0) = -4$$

$$f'''(x) = \frac{16}{(1+2x)^3} \quad\Rightarrow\quad f'''(0) = 16$$

**Step 2 — Apply the Maclaurin series formula.**

$$f(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3 + \dots$$

$$f(x) = 0 + 2x + \frac{-4}{2}x^2 + \frac{16}{6}x^3 + \dots$$

$$f(x) = 2x - 2x^2 + \frac{8}{3}x^3 + \dots$$

**Step 3 — Check against the standard series.** The standard result \(\ln(1+u) = u - \dfrac{u^2}{2} + \dfrac{u^3}{3} - \dots\) with \(u = 2x\) gives:

$$\ln(1+2x) = 2x - \frac{(2x)^2}{2} + \frac{(2x)^3}{3} - \dots = 2x - 2x^2 + \frac{8}{3}x^3 - \dots$$

This matches the result from direct differentiation, confirming the expansion. A numerical check at \(x = 0.01\) also agrees: \(\ln(1.02) = 0.019803\ldots\) versus the series estimate \(2(0.01) - 2(0.01)^2 + \frac{8}{3}(0.01)^3 = 0.019803\ldots\), matching to 6 decimal places.

**Common mistake:** forgetting the chain-rule factor of 2 when differentiating \(\ln(1+2x)\) — writing \(f'(x) = \dfrac{1}{1+2x}\) instead of \(\dfrac{2}{1+2x}\). This error compounds through every subsequent derivative and gives the series for \(\ln(1+x)\) instead.

## Answer

$$\ln(1+2x) = 2x - 2x^2 + \frac{8}{3}x^3 + \dots$$
