---
title: Finding unknown coefficients using the remainder theorem
subject: amath
topic: Remainder Theorem
level: O-Level
difficulty: Medium
description: Use the remainder theorem with two given remainders to find two unknown coefficients in a cubic polynomial, then find a third remainder.
date: 2026-07-16
---

## Question

The polynomial \( p(x) = 2x^3 - x^2 + ax + b \), where \(a\) and \(b\) are constants, leaves a remainder of 4 when divided by \((x - 1)\) and a remainder of \(-5\) when divided by \((x + 2)\).

(a) Find the values of \(a\) and \(b\).

(b) Hence find the remainder when \(p(x)\) is divided by \((x - 3)\).

## Solution

**Setting up equations with the remainder theorem.** By the remainder theorem, dividing \(p(x)\) by \((x - k)\) leaves remainder \(p(k)\).

Divided by \((x-1)\), remainder is \(p(1) = 4\):
$$2(1)^3 - (1)^2 + a(1) + b = 4$$
$$2 - 1 + a + b = 4 \implies a + b = 3 \quad \text{...(1)}$$

Divided by \((x+2)\), remainder is \(p(-2) = -5\):
$$2(-2)^3 - (-2)^2 + a(-2) + b = -5$$
$$-16 - 4 - 2a + b = -5 \implies -2a + b = 15 \quad \text{...(2)}$$

**Solving simultaneously.** Subtracting (2) from (1):
$$(a + b) - (-2a + b) = 3 - 15$$
$$3a = -12 \implies a = -4$$

Substituting into (1): \(-4 + b = 3 \implies b = 7\).

**Check.** With \(a = -4, b = 7\): \(p(x) = 2x^3 - x^2 - 4x + 7\).
\(p(1) = 2 - 1 - 4 + 7 = 4\) ✓
\(p(-2) = -16 - 4 + 8 + 7 = -5\) ✓
Both given remainders match, so \(a = -4\) and \(b = 7\) are correct.

**(b) Remainder when divided by \((x-3)\).** By the remainder theorem this is \(p(3)\):
$$p(3) = 2(3)^3 - (3)^2 - 4(3) + 7 = 54 - 9 - 12 + 7 = 40$$

**Common mistake:** sign errors when substituting a negative value of \(x\) into an odd power, e.g. writing \((-2)^3 = 8\) instead of \(-8\). Always evaluate the sign of each power separately before multiplying by its coefficient.

## Answer

(a) \(a = -4\), \(b = 7\).

(b) The remainder when \(p(x)\) is divided by \((x-3)\) is **40**.
