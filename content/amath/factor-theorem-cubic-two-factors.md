---
title: Factor theorem — finding a and b in a cubic given two of its factors
subject: amath
topic: Factor Theorem
level: O-Level
difficulty: Medium
description: Use the factor theorem to find unknown coefficients in a cubic polynomial given two of its factors, then factorise it completely.
date: 2026-07-10
---

## Question

It is given that \( f(x) = 2x^3 + ax^2 + bx - 12 \), where \(a\) and \(b\) are constants, has \( (x-2) \) and \( (x+1) \) as factors.

(a) Find the values of \(a\) and \(b\).

(b) Hence factorise \( f(x) \) completely.

## Solution

**(a) Finding a and b**

Since \( (x - 2) \) is a factor, the factor theorem gives \( f(2) = 0 \):
$$f(2) = 2(2)^3 + a(2)^2 + b(2) - 12 = 16 + 4a + 2b - 12 = 4a + 2b + 4$$

Setting this to zero and dividing by 2:
$$2a + b = -2 \quad \text{...(1)}$$

Since \( (x + 1) \) is a factor, \( f(-1) = 0 \):
$$f(-1) = 2(-1)^3 + a(-1)^2 + b(-1) - 12 = -2 + a - b - 12 = a - b - 14$$

Setting this to zero:
$$a - b = 14 \quad \text{...(2)}$$

Adding (1) and (2): \( 3a = 12 \), so \( a = 4 \). Substituting into (2): \( b = 4 - 14 = -10 \).

**Check:** \( f(x) = 2x^3 + 4x^2 - 10x - 12 \). Then \( f(2) = 16+16-20-12=0 \) ✓ and \( f(-1) = -2+4+10-12=0 \) ✓.

**(b) Factorising completely**

With \(a=4, b=-10\), \( f(x) = 2x^3 + 4x^2 - 10x - 12 \). Since \( (x-2) \) and \( (x+1) \) are both factors, \( (x-2)(x+1) = x^2 - x - 2 \) divides \( f(x) \) exactly. Dividing:
$$f(x) \div (x^2 - x - 2) = 2x + 6$$

because \( (x^2-x-2)(2x+6) = 2x^3 + 6x^2 - 2x^2 - 6x - 4x - 12 = 2x^3 + 4x^2 - 10x - 12 \), which matches \( f(x) \).

So \( f(x) = (x-2)(x+1)(2x+6) = 2(x-2)(x+1)(x+3) \).

**Check by expansion:** \( (x-2)(x+1) = x^2 - x - 2 \). Then \( (x^2-x-2)(x+3) = x^3 + 2x^2 - 5x - 6 \). Multiplying by 2 gives \( 2x^3+4x^2-10x-12 \), which is exactly \( f(x) \). ✓

**Common mistake:** Substituting the wrong sign when using \( (x+1) \) as a factor — students often compute \(f(1)\) instead of \(f(-1)\). Remember \( (x+1) \) is a factor means the root is \( x = -1 \), not \( x = 1 \).

## Answer

\( a = 4 \), \( b = -10 \), and \( f(x) = 2(x-2)(x+1)(x+3) \).
