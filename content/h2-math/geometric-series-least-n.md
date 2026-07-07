---
title: Geometric series — finding the least n for Sₙ to exceed 11.9
subject: h2-math
topic: Sequences and Series
level: A-Level
difficulty: Medium
description: A geometric series has first term 3 and sum to infinity 12. Find the common ratio and the least number of terms for the sum to exceed 11.9.
date: 2026-07-07
---

## Question

A geometric series has first term \(a = 3\) and sum to infinity \(S_\infty = 12\).

1. Find the common ratio \(r\).
2. Find the least value of \(n\) for which the sum of the first \(n\) terms exceeds 11.9.

## Solution

**Part 1 — Common ratio.** Using \(S_\infty = \dfrac{a}{1-r}\):

$$12 = \frac{3}{1-r} \quad\Rightarrow\quad 1 - r = \frac{3}{12} = \frac{1}{4} \quad\Rightarrow\quad r = \frac{3}{4}$$

Since \(|r| = 0.75 \lt 1\), the sum to infinity is valid. ✓

**Part 2 — Least \(n\).** The sum of the first \(n\) terms is

$$S_n = \frac{a(1 - r^n)}{1 - r} = \frac{3\left(1 - (3/4)^n\right)}{1/4} = 12\left(1 - \left(\tfrac{3}{4}\right)^n\right)$$

We require \(S_n > 11.9\):

$$12\left(1 - \left(\tfrac{3}{4}\right)^n\right) > 11.9$$

$$1 - \left(\tfrac{3}{4}\right)^n > \frac{11.9}{12}$$

$$\left(\tfrac{3}{4}\right)^n \lt \frac{0.1}{12} = \frac{1}{120}$$

Take logarithms of both sides. **Careful:** \(\ln\frac{3}{4}\) is negative, so the inequality flips when dividing:

$$n \ln\tfrac{3}{4} \lt \ln\tfrac{1}{120} \quad\Rightarrow\quad n > \frac{\ln(1/120)}{\ln(3/4)} = \frac{-4.7875}{-0.28768} \approx 16.64$$

So the least integer is \(n = 17\).

**Check:** \((3/4)^{17} \approx 0.00752 \lt \frac{1}{120} \approx 0.00833\) ✓ and \((3/4)^{16} \approx 0.0100 > 0.00833\) ✓

## Answer

1. \(r = \dfrac{3}{4}\)
2. Least \(n = 17\)
