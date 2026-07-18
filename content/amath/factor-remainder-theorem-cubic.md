---
title: Using the factor and remainder theorems to factorise a cubic completely
subject: amath
topic: Factor and Remainder Theorem
level: O-Level
difficulty: Medium
description: Use the factor theorem and remainder theorem together to find unknown coefficients in a cubic, then factorise it completely.
date: 2026-07-19
---

## Question

The cubic polynomial \( f(x) = 2x^3 + ax^2 - 11x + c \) has \( (x - 2) \) as a factor, and leaves a remainder of 6 when divided by \( (x + 1) \).

(a) Find the values of \(a\) and \(c\).

(b) Hence factorise \(f(x)\) completely, and solve \(f(x) = 0\).

## Solution

**Part (a).**

Since \( (x-2) \) is a factor, the factor theorem gives \( f(2) = 0 \):

$$f(2) = 2(2)^3 + a(2)^2 - 11(2) + c = 16 + 4a - 22 + c = 4a + c - 6 = 0$$

$$\Rightarrow 4a + c = 6 \quad \text{...(1)}$$

Since dividing by \( (x+1) \) leaves remainder 6, the remainder theorem gives \( f(-1) = 6 \):

$$f(-1) = 2(-1)^3 + a(-1)^2 - 11(-1) + c = -2 + a + 11 + c = a + c + 9 = 6$$

$$\Rightarrow a + c = -3 \quad \text{...(2)}$$

Subtracting (2) from (1): \( 3a = 9 \), so \( a = 3 \). Substituting into (2): \( c = -3 - 3 = -6 \).

So \( f(x) = 2x^3 + 3x^2 - 11x - 6 \).

**Part (b).**

Divide \(f(x)\) by \( (x - 2) \) using long division:

$$2x^3 + 3x^2 - 11x - 6 = (x-2)(2x^2 + 7x + 3)$$

Factorise the quadratic: \( 2x^2 + 7x + 3 = (2x+1)(x+3) \).

$$f(x) = (x-2)(2x+1)(x+3)$$

Setting \(f(x) = 0\):

$$x = 2, \qquad x = -\tfrac{1}{2}, \qquad x = -3$$

**Check.** Substitute \(a=3, c=-6\) back: \(f(2) = 16+12-22-6 = 0\) ✓, and \(f(-1) = -2+3+11-6 = 6\) ✓, matching both given conditions. Expanding \((x-2)(2x+1)(x+3)\) also returns \(2x^3+3x^2-11x-6\), confirming the factorisation.

**Common mistake:** writing the root from \((2x+1)\) as \(x = 2\) or \(x=1\) instead of \(x = -\tfrac{1}{2}\) — students often forget to divide by the coefficient of \(x\) when reading off the root of a linear factor that isn't monic.

## Answer

(a) \( a = 3 \), \( c = -6 \).

(b) \( f(x) = (x-2)(2x+1)(x+3) \); the roots of \(f(x)=0\) are \( x = 2,\ -\tfrac{1}{2},\ -3 \).
