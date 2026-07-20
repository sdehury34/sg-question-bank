---
title: Partial fractions of (5x + 7) / ((x + 1)(x + 2)²) with a repeated factor
subject: amath
topic: Partial Fractions
level: O-Level
difficulty: Medium
description: Express (5x + 7)/((x + 1)(x + 2)²) in partial fractions, working through the repeated linear factor case step by step.
date: 2026-07-21
---

## Question

Express \( \dfrac{5x + 7}{(x + 1)(x + 2)^2} \) in partial fractions.

## Solution

**Set up the form.** Since \((x+2)\) is a repeated linear factor, the partial fraction form must include a term for \((x+2)\) **and** a term for \((x+2)^2\):

$$\frac{5x+7}{(x+1)(x+2)^2} = \frac{A}{x+1} + \frac{B}{x+2} + \frac{C}{(x+2)^2}$$

**Clear denominators.** Multiplying both sides by \((x+1)(x+2)^2\):

$$5x + 7 = A(x+2)^2 + B(x+1)(x+2) + C(x+1)$$

**Substitute convenient values of \(x\)** to knock out terms:

- Let \(x = -1\): \(5(-1)+7 = A(1)^2 \Rightarrow 2 = A \Rightarrow A = 2\)
- Let \(x = -2\): \(5(-2)+7 = C(-1) \Rightarrow -3 = -C \Rightarrow C = 3\)

**Find \(B\)** by comparing coefficients of \(x^2\) on both sides. On the right, the only \(x^2\) terms come from \(A(x+2)^2\) and \(B(x+1)(x+2)\), giving coefficient \(A + B\); on the left the coefficient of \(x^2\) is \(0\):

$$0 = A + B \Rightarrow B = -A = -2$$

**Check** by substituting \(x = 0\) into the original identity:

$$\text{LHS: } 5(0)+7 = 7$$

$$\text{RHS: } A(2)^2 + B(1)(2) + C(1) = 4(2) + 2(-2) + 3 = 8 - 4 + 3 = 7 \checkmark$$

A second check at \(x = 1\): LHS \(= \dfrac{12}{(2)(9)} = \dfrac{2}{3}\); RHS \(= \dfrac{2}{2} + \dfrac{-2}{3} + \dfrac{3}{9} = 1 - \dfrac{2}{3} + \dfrac{1}{3} = \dfrac{2}{3}\ \checkmark\)

**Common mistake:** writing only a single term \(\dfrac{B}{x+2}\) for the repeated factor \((x+2)^2\) instead of **two** terms, \(\dfrac{B}{x+2} + \dfrac{C}{(x+2)^2}\). Omitting the \((x+2)^2\) term leaves one unknown short and makes the identity impossible to satisfy for all \(x\).

## Answer

$$\frac{5x+7}{(x+1)(x+2)^2} = \frac{2}{x+1} - \frac{2}{x+2} + \frac{3}{(x+2)^2}$$
