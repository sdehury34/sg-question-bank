---
title: Finding the modulus-argument form of z = √3 − i and evaluating z⁶
subject: h2-math
topic: Complex Numbers
level: A-Level
difficulty: Medium
description: Convert a complex number to modulus-argument form and apply De Moivre's theorem to evaluate its sixth power.
date: 2026-07-11
---

## Question

Express \(z = \sqrt{3} - i\) in the form \(r(\cos\theta + i\sin\theta)\), where \(r > 0\) and \(-\pi < \theta \le \pi\). Hence use De Moivre's theorem to find \(z^6\), giving your answer in the form \(a + bi\).

## Solution

**Step 1 — Find the modulus.**

$$r = |z| = \sqrt{(\sqrt{3})^2 + (-1)^2} = \sqrt{3+1} = \sqrt{4} = 2$$

**Step 2 — Find the argument.** The real part \(\sqrt{3} > 0\) and the imaginary part \(-1 < 0\), so \(z\) lies in the **fourth quadrant**. The basic angle is

$$\alpha = \arctan\left(\frac{1}{\sqrt{3}}\right) = \frac{\pi}{6}$$

Since \(z\) is in the fourth quadrant, the principal argument is negative:

$$\theta = -\frac{\pi}{6}$$

So

$$z = 2\left(\cos\left(-\frac{\pi}{6}\right) + i\sin\left(-\frac{\pi}{6}\right)\right)$$

**Step 3 — Apply De Moivre's theorem.** For \(z = r(\cos\theta + i\sin\theta)\),

$$z^n = r^n(\cos n\theta + i\sin n\theta)$$

With \(n = 6\):

$$z^6 = 2^6\left(\cos\left(6 \times -\frac{\pi}{6}\right) + i\sin\left(6\times -\frac{\pi}{6}\right)\right) = 64\left(\cos(-\pi) + i\sin(-\pi)\right)$$

**Step 4 — Evaluate.**

$$\cos(-\pi) = -1, \qquad \sin(-\pi) = 0$$

$$z^6 = 64(-1 + 0i) = -64$$

**Check by direct expansion.** Computing \(z^2\), \(z^3\) and squaring:

$$z^2 = (\sqrt3 - i)^2 = 3 - 2\sqrt3\,i + i^2 = 2 - 2\sqrt3\,i$$

$$z^3 = z^2 \cdot z = (2-2\sqrt3\,i)(\sqrt3-i) = 2\sqrt3 - 2i - 6i + 2\sqrt3\,i^2 = -8i$$

$$z^6 = (z^3)^2 = (-8i)^2 = 64\,i^2 = -64 \checkmark$$

This matches the De Moivre result exactly.

**Common mistake:** using \(\theta = \arctan(-1/\sqrt3) \) blindly from a calculator without checking the quadrant. A calculator's `arctan` only returns values in \((-\pi/2, \pi/2)\), so for points in the second or third quadrant this gives the wrong angle unless you adjust by \(\pm\pi\). Here the point happens to lie in the fourth quadrant where the raw arctan value is already correct, but this must be checked every time, not assumed.

## Answer

\(z = 2\left(\cos\left(-\dfrac{\pi}{6}\right) + i\sin\left(-\dfrac{\pi}{6}\right)\right)\), and \(z^6 = -64\).
