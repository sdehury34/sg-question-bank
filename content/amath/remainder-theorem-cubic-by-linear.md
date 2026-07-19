---
title: Remainder when a cubic polynomial is divided by (2x + 1)
subject: amath
topic: Remainder and Factor Theorem
level: O-Level
difficulty: Medium
description: Use the Remainder Theorem to find the remainder when 2x³ − 5x² + 4x − 3 is divided by (2x + 1), checked by long division.
date: 2026-07-20
---

## Question

Find the remainder when \( f(x) = 2x^3 - 5x^2 + 4x - 3 \) is divided by \( (2x + 1) \).

## Solution

By the Remainder Theorem, when a polynomial \( f(x) \) is divided by \( (ax - b) \), the remainder equals \( f(b/a) \). Here \( (2x+1) = 0 \) gives \( x = -\dfrac{1}{2} \), so the remainder is \( f(-\tfrac{1}{2}) \).

$$
f\left(-\tfrac{1}{2}\right) = 2\left(-\tfrac{1}{2}\right)^3 - 5\left(-\tfrac{1}{2}\right)^2 + 4\left(-\tfrac{1}{2}\right) - 3
$$

$$
= 2\left(-\tfrac{1}{8}\right) - 5\left(\tfrac{1}{4}\right) - 2 - 3 = -\tfrac{1}{4} - \tfrac{5}{4} - 5 = -\tfrac{6}{4} - 5 = -\tfrac{3}{2} - 5 = -\tfrac{13}{2}
$$

**Check by long division.** Dividing \( 2x^3 - 5x^2 + 4x - 3 \) by \( (2x+1) \):

- \( 2x^3 \div 2x = x^2 \). Subtracting \( x^2(2x+1) = 2x^3 + x^2 \) leaves \( -6x^2 + 4x - 3 \).
- \( -6x^2 \div 2x = -3x \). Subtracting \( -3x(2x+1) = -6x^2 - 3x \) leaves \( 7x - 3 \).
- \( 7x \div 2x = \tfrac{7}{2} \). Subtracting \( \tfrac{7}{2}(2x+1) = 7x + \tfrac{7}{2} \) leaves \( -3 - \tfrac{7}{2} = -\tfrac{13}{2} \).

So \( f(x) = (2x+1)\left(x^2 - 3x + \tfrac{7}{2}\right) - \tfrac{13}{2} \), confirming the remainder is \( -\tfrac{13}{2} \).

**Common mistake:** Setting \( 2x + 1 = 0 \) and then substituting \( x = -1 \) (dividing by the wrong part of the equation) instead of the correct root \( x = -\tfrac{1}{2} \). Always solve the divisor for \( x \) first.

## Answer

Remainder \( = -\dfrac{13}{2} \) (or \( -6.5 \)).
