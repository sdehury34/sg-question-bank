---
title: Solving log₃x + log₃(x − 2) = 1
subject: amath
topic: Logarithms
level: O-Level
difficulty: Easy
description: Step-by-step solution to the logarithmic equation log₃x + log₃(x − 2) = 1, including the domain check that rejects the extraneous root.
date: 2026-07-12
---

## Question

Solve the equation

$$\log_3 x + \log_3(x - 2) = 1$$

giving the value(s) of \( x \).

## Solution

Combine the two logarithms on the left using \( \log_a m + \log_a n = \log_a(mn) \):

$$\log_3\big[x(x-2)\big] = 1$$

Convert to index form (base 3):

$$x(x-2) = 3^1 = 3$$

$$x^2 - 2x - 3 = 0$$

Factorise:

$$(x-3)(x+1) = 0$$

$$x = 3 \quad \text{or} \quad x = -1$$

**Domain check.** Both \( x \) and \( x-2 \) must be strictly positive for the original logarithms to be defined, so we need \( x > 2 \).

- \( x = -1 \): gives \( \log_3(-1) \), undefined — **rejected**.
- \( x = 3 \): satisfies \( x > 2 \) — **valid**.

**Verification by substitution:** \( \log_3 3 + \log_3(3-2) = \log_3 3 + \log_3 1 = 1 + 0 = 1 \). ✓

**Common mistake:** Students solve the quadratic correctly but forget to check the domain of the original logarithmic equation, giving both \( x = 3 \) and \( x = -1 \) as final answers. Any root that makes an argument of a log zero or negative must be rejected.

## Answer

\( x = 3 \)
