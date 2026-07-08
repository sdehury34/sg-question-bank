---
title: Finding the cube roots of 8i using De Moivre's Theorem
subject: h2-math
topic: Complex Numbers
level: A-Level
difficulty: Hard
description: Use De Moivre's Theorem to find all three cube roots of the complex number 8i in exact modulus-argument and cartesian form.
date: 2026-07-09
---

## Question

Find the three cube roots of \(z = 8i\), giving each root in the form \(r\,\text{cis}\,\theta\) with \(\theta\) in radians in the range \(-\pi < \theta \le \pi\). Hence express each root in cartesian form \(a + bi\).

## Solution

**Step 1 — Write \(z\) in modulus-argument form.** Since \(z = 8i\) lies on the positive imaginary axis, \(|z| = 8\) and \(\arg(z) = \dfrac{\pi}{2}\), so

$$z = 8\,\text{cis}\left(\frac{\pi}{2} + 2k\pi\right), \quad k \in \mathbb{Z}$$

**Step 2 — Apply De Moivre's Theorem for a cube root.** If \(w = r\,\text{cis}\,\theta\) satisfies \(w^3 = z\), then

$$r^3 = 8 \implies r = 2, \qquad 3\theta = \frac{\pi}{2} + 2k\pi \implies \theta = \frac{\pi}{6} + \frac{2k\pi}{3}$$

**Step 3 — Take \(k = -1, 0, 1\)** to generate the three distinct roots with argument in \((-\pi, \pi]\):

- \(k = 0\): \(\theta = \dfrac{\pi}{6}\) → \(w_0 = 2\,\text{cis}\dfrac{\pi}{6}\)
- \(k = 1\): \(\theta = \dfrac{\pi}{6} + \dfrac{2\pi}{3} = \dfrac{5\pi}{6}\) → \(w_1 = 2\,\text{cis}\dfrac{5\pi}{6}\)
- \(k = -1\): \(\theta = \dfrac{\pi}{6} - \dfrac{2\pi}{3} = -\dfrac{\pi}{2}\) → \(w_2 = 2\,\text{cis}\left(-\dfrac{\pi}{2}\right)\)

**Step 4 — Convert to cartesian form.**

$$w_0 = 2\left(\cos\frac{\pi}{6} + i\sin\frac{\pi}{6}\right) = 2\left(\frac{\sqrt3}{2} + \frac{i}{2}\right) = \sqrt3 + i$$

$$w_1 = 2\left(\cos\frac{5\pi}{6} + i\sin\frac{5\pi}{6}\right) = 2\left(-\frac{\sqrt3}{2} + \frac{i}{2}\right) = -\sqrt3 + i$$

$$w_2 = 2\left(\cos\left(-\frac{\pi}{2}\right) + i\sin\left(-\frac{\pi}{2}\right)\right) = -2i$$

**Check:** cube \(w_0 = \sqrt3 + i\) directly. First, \((\sqrt3 + i)^2 = 3 + 2\sqrt3\,i - 1 = 2 + 2\sqrt3\,i\). Then

$$(\sqrt3+i)^3 = (2 + 2\sqrt3\,i)(\sqrt3 + i) = 2\sqrt3 + 2i + 6i + 2\sqrt3\,i^2 = 2\sqrt3 - 2\sqrt3 + 8i = 8i \checkmark$$

As a further check, the three cube roots of a nonzero number always sum to zero:

$$(\sqrt3 + i) + (-\sqrt3 + i) + (-2i) = 0 \checkmark$$

Both checks confirm the roots are correct.

**Common mistake:** finding only \(w_0 = 2\,\text{cis}\dfrac{\pi}{6}\) and stopping there. A cube root equation has **three** roots — students must add \(2k\pi\) to the argument before dividing by 3, not after, otherwise the other two roots are missed.

## Answer

$$w_0 = 2\,\text{cis}\frac{\pi}{6} = \sqrt3 + i, \qquad w_1 = 2\,\text{cis}\frac{5\pi}{6} = -\sqrt3 + i, \qquad w_2 = 2\,\text{cis}\left(-\frac{\pi}{2}\right) = -2i$$
