---
title: Evaluating ∫₀¹ x e²ˣ dx using integration by parts
subject: h2-math
topic: Integration Techniques
level: A-Level
difficulty: Medium
description: Evaluate the definite integral of x e^(2x) from 0 to 1 using integration by parts, giving an exact answer.
date: 2026-07-07
---

## Question

Using integration by parts, evaluate \(\displaystyle\int_0^1 x e^{2x}\, dx\), giving your answer in exact form.

## Solution

**Step 1 — Choose \(u\) and \(dv\).** Following LIATE (algebraic before exponential), let

$$u = x, \qquad \frac{dv}{dx} = e^{2x}$$

so that

$$\frac{du}{dx} = 1, \qquad v = \frac{1}{2}e^{2x}$$

**Step 2 — Apply the by-parts formula** \(\int u\,dv = uv - \int v\,du\):

$$\int_0^1 x e^{2x}\,dx = \left[\frac{x}{2}e^{2x}\right]_0^1 - \int_0^1 \frac{1}{2}e^{2x}\,dx$$

**Step 3 — Evaluate each piece.**

$$\left[\frac{x}{2}e^{2x}\right]_0^1 = \frac{1}{2}e^{2} - 0 = \frac{e^2}{2}$$

$$\int_0^1 \frac{1}{2}e^{2x}\,dx = \left[\frac{1}{4}e^{2x}\right]_0^1 = \frac{e^2}{4} - \frac{1}{4}$$

**Step 4 — Combine.**

$$\int_0^1 x e^{2x}\,dx = \frac{e^2}{2} - \left(\frac{e^2}{4} - \frac{1}{4}\right) = \frac{e^2}{4} + \frac{1}{4}$$

**Common mistake:** integrating \(e^{2x}\) to \(e^{2x}\) instead of \(\frac{1}{2}e^{2x}\) — remember to divide by the derivative of the inner function.

## Answer

$$\int_0^1 x e^{2x}\,dx = \frac{e^2 + 1}{4} \approx 2.10$$
