---
title: Solving dy/dx = 2x(y − 1) with initial condition y(0) = 3
subject: h2-math
topic: Differential Equations
level: A-Level
difficulty: Medium
description: Find the general and particular solution of the separable differential equation dy/dx = 2x(y − 1) given y = 3 when x = 0.
date: 2026-07-23
---

## Question

Find the particular solution of the differential equation

$$\frac{dy}{dx} = 2x(y-1)$$

given that \(y = 3\) when \(x = 0\). Express \(y\) in terms of \(x\).

## Solution

**Step 1 — Separate the variables.** Since \(y \neq 1\), divide both sides by \(y - 1\):

$$\frac{1}{y-1}\,dy = 2x\,dx$$

**Step 2 — Integrate both sides.**

$$\int \frac{1}{y-1}\,dy = \int 2x\,dx$$

$$\ln|y-1| = x^2 + C$$

**Step 3 — Make \(y\) the subject.**

$$|y-1| = e^{x^2+C} = e^C e^{x^2}$$

$$y - 1 = A e^{x^2}, \qquad \text{where } A = \pm e^C \text{ is a non-zero arbitrary constant}$$

So the general solution is

$$y = 1 + Ae^{x^2}$$

**Step 4 — Apply the initial condition \(y(0) = 3\).**

$$3 = 1 + Ae^{0} = 1 + A \implies A = 2$$

$$y = 1 + 2e^{x^2}$$

**Check by substitution:** differentiating, \(\dfrac{dy}{dx} = 4x e^{x^2}\). The right-hand side of the original equation is \(2x(y-1) = 2x(2e^{x^2}) = 4xe^{x^2}\), which matches. Also \(y(0) = 1 + 2e^0 = 3\) as required.

**Common mistake:** dropping the modulus sign when integrating \(\frac{1}{y-1}\) (writing \(\ln(y-1)\) instead of \(\ln|y-1|\)), or forgetting to introduce the arbitrary constant \(A\) before applying the initial condition, which makes it impossible to fit \(y(0)=3\).

## Answer

$$y = 1 + 2e^{x^2}$$
