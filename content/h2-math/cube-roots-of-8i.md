---
title: Finding the cube roots of 8i in exponential form
subject: h2-math
topic: Complex Numbers
level: A-Level
difficulty: Hard
description: Find all three cube roots of the complex number 8i, expressed in exponential form re^(iθ) with θ in the principal range.
date: 2026-07-20
---

## Question

Find the three cube roots of \( 8i \), giving each answer in the form \( re^{i\theta} \), where \( r > 0 \) and \( -\pi < \theta \leq \pi \).

## Solution

First write \( z = 8i \) in exponential form. Since \( z \) lies on the positive imaginary axis, \( |z| = 8 \) and \( \arg(z) = \dfrac{\pi}{2} \), so

$$
z = 8e^{i\left(\frac{\pi}{2} + 2k\pi\right)}, \quad k \in \mathbb{Z}.
$$

To find the cube roots, solve \( w^3 = z \), so \( w = z^{1/3} \):

$$
w = 8^{1/3} \, e^{i\left(\frac{\pi/2 + 2k\pi}{3}\right)} = 2e^{i\left(\frac{\pi}{6} + \frac{2k\pi}{3}\right)}, \quad k = 0, 1, 2.
$$

Substituting \( k = 0, 1, 2 \):

- \( k = 0 \): \( \theta = \dfrac{\pi}{6} \) → \( w_0 = 2e^{i\pi/6} \)
- \( k = 1 \): \( \theta = \dfrac{\pi}{6} + \dfrac{2\pi}{3} = \dfrac{5\pi}{6} \) → \( w_1 = 2e^{i5\pi/6} \)
- \( k = 2 \): \( \theta = \dfrac{\pi}{6} + \dfrac{4\pi}{3} = \dfrac{3\pi}{2} \), which is outside \( (-\pi, \pi] \). Subtracting \( 2\pi \) gives \( \theta = -\dfrac{\pi}{2} \) → \( w_2 = 2e^{-i\pi/2} \)

**Check:** Cube each root and confirm it returns to \( 8i \).
\( \left(2e^{i\pi/6}\right)^3 = 8e^{i\pi/2} = 8i \). ✓
\( \left(2e^{i5\pi/6}\right)^3 = 8e^{i5\pi/2} = 8e^{i(5\pi/2 - 2\pi)} = 8e^{i\pi/2} = 8i \). ✓
\( \left(2e^{-i\pi/2}\right)^3 = 8e^{-i3\pi/2} = 8e^{i(-3\pi/2 + 2\pi)} = 8e^{i\pi/2} = 8i \). ✓

As a further check in Cartesian form, \( 2e^{i\pi/6} = \sqrt{3} + i \), and \( (\sqrt{3}+i)^2 = 2 + 2\sqrt{3}i \), so \( (\sqrt{3}+i)^3 = (2+2\sqrt{3}i)(\sqrt{3}+i) = 2\sqrt{3} + 2i + 6i - 2\sqrt{3} = 8i \), matching exactly.

**Common mistake:** Finding only one cube root (forgetting that a non-zero complex number has exactly 3 distinct cube roots, spaced \( \dfrac{2\pi}{3} \) apart), or leaving an angle like \( \dfrac{3\pi}{2} \) unadjusted instead of converting it into the principal range \( (-\pi, \pi] \).

## Answer

The three cube roots are \( 2e^{i\pi/6} \), \( 2e^{i5\pi/6} \), and \( 2e^{-i\pi/2} \).
