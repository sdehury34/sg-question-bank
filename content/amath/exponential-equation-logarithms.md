---
title: Solving 5^(2x−1) = 3^(x+2) using logarithms
subject: amath
topic: Logarithmic and Exponential Equations
level: O-Level
difficulty: Medium
description: Solve the exponential equation 5^(2x−1) = 3^(x+2) for x by taking logarithms of both sides, giving the answer to 3 significant figures.
date: 2026-07-15
---

## Question

Solve for \(x\), giving your answer correct to 3 significant figures:

$$5^{2x-1} = 3^{x+2}$$

## Solution

**Step 1 — Take logarithms of both sides.** Since the unknown is in the exponent on both sides, take \(\ln\) (or \(\lg\)) of both sides:

$$\ln\left(5^{2x-1}\right) = \ln\left(3^{x+2}\right)$$

**Step 2 — Bring the exponents down** using \(\ln(a^n) = n\ln a\):

$$(2x-1)\ln 5 = (x+2)\ln 3$$

**Step 3 — Expand and collect all \(x\) terms on one side.**

$$2x\ln 5 - \ln 5 = x \ln 3 + 2\ln 3$$

$$2x\ln 5 - x\ln 3 = 2\ln 3 + \ln 5$$

$$x(2\ln 5 - \ln 3) = 2\ln 3 + \ln 5$$

**Step 4 — Solve for \(x\).**

$$x = \frac{2\ln 3 + \ln 5}{2\ln 5 - \ln 3}$$

Using \(\ln 3 = 1.098612\ldots\) and \(\ln 5 = 1.609438\ldots\):

$$x = \frac{2(1.098612) + 1.609438}{2(1.609438) - 1.098612} = \frac{3.806663}{2.120264} = 1.79537\ldots$$

**Step 5 — Check.** Substituting the unrounded value \(x = 1.79537\) back into the original equation:

$$5^{2(1.79537)-1} = 5^{2.59074} \approx 64.69, \qquad 3^{1.79537+2} = 3^{3.79537} \approx 64.69$$

Both sides agree, confirming the solution.

**Common mistake:** taking logs of each term separately (e.g. writing \(\ln 5^{2x} - \ln 1\) or splitting \(2x-1\) as two separate powers) instead of treating \((2x-1)\) as a single exponent before expanding — this is a direct application of \(\ln(a^n) = n \ln a\) with \(n = 2x-1\) as one bracketed quantity.

## Answer

$$x = 1.80 \text{ (3 s.f.)}$$
