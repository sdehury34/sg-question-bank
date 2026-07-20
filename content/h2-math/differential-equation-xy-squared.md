---
title: Solving dy/dx = xy² by separation of variables with y(0) = 1
subject: h2-math
topic: Differential Equations
level: A-Level
difficulty: Medium
description: Solve the first-order differential equation dy/dx = xy² given y = 1 when x = 0, using separation of variables.
date: 2026-07-21
---

## Question

Given that \( \dfrac{dy}{dx} = xy^2 \) and \(y = 1\) when \(x = 0\), find \(y\) in terms of \(x\).

## Solution

**Separate the variables.** Since the right-hand side factors as a function of \(x\) times a function of \(y\), divide both sides by \(y^2\) and multiply by \(dx\):

$$\frac{1}{y^2}\, dy = x\, dx$$

**Integrate both sides:**

$$\int y^{-2}\, dy = \int x\, dx$$

$$-\frac{1}{y} = \frac{x^2}{2} + C$$

**Apply the initial condition** \(y = 1\) when \(x = 0\):

$$-\frac{1}{1} = \frac{0^2}{2} + C \Rightarrow C = -1$$

**Substitute back:**

$$-\frac{1}{y} = \frac{x^2}{2} - 1$$

**Rearrange for \(y\).** Multiply both sides by \(-1\):

$$\frac{1}{y} = 1 - \frac{x^2}{2} = \frac{2 - x^2}{2}$$

$$y = \frac{2}{2 - x^2}$$

**Check.** At \(x=0\): \(y = \dfrac{2}{2} = 1\ \checkmark\), matching the initial condition.

Differentiating \(y = \dfrac{2}{2-x^2} = 2(2-x^2)^{-1}\) using the chain rule:

$$\frac{dy}{dx} = 2 \times (-1)(2-x^2)^{-2} \times (-2x) = \frac{4x}{(2-x^2)^2}$$

Compare with \(xy^2 = x\left(\dfrac{2}{2-x^2}\right)^2 = \dfrac{4x}{(2-x^2)^2}\). This matches \(\dfrac{dy}{dx}\) exactly, confirming the solution. \(\checkmark\)

**Common mistake:** integrating \(y^{-2}\) as \(\dfrac{y^{-1}}{-1} = y^{-1}\) instead of \(-y^{-1}\) — i.e. dropping the negative sign from the power rule. This flips the sign of the constant of integration and gives an incorrect final expression for \(y\).

## Answer

$$y = \frac{2}{2 - x^2}$$
