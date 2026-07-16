---
title: Finding the modulus and argument of a product and quotient of complex numbers
subject: h2-math
topic: Complex Numbers
level: A-Level
difficulty: Medium
description: Express the product and quotient of two complex numbers in the form re^{iθ} using modulus-argument rules.
date: 2026-07-17
---

## Question

Let \(z_1 = 1 + i\) and \(z_2 = \sqrt{3} - i\).

(a) Find the modulus and argument of \(z_1\) and of \(z_2\).

(b) Hence express \(z_1 z_2\) and \(\dfrac{z_1}{z_2}\) in the form \(re^{i\theta}\), where \(r > 0\) and \(-\pi < \theta \le \pi\).

## Solution

**Step 1 — Modulus and argument of \(z_1\) and \(z_2\).**

$$|z_1| = \sqrt{1^2 + 1^2} = \sqrt{2}, \qquad \arg(z_1) = \arctan\left(\frac{1}{1}\right) = \frac{\pi}{4}$$

\(z_2 = \sqrt3 - i\) lies in the fourth quadrant:

$$|z_2| = \sqrt{(\sqrt3)^2 + (-1)^2} = \sqrt{4} = 2, \qquad \arg(z_2) = -\arctan\left(\frac{1}{\sqrt3}\right) = -\frac{\pi}{6}$$

**Step 2 — Multiply moduli, add arguments.**

$$|z_1 z_2| = \sqrt2 \times 2 = 2\sqrt2$$

$$\arg(z_1 z_2) = \frac{\pi}{4} + \left(-\frac{\pi}{6}\right) = \frac{3\pi}{12} - \frac{2\pi}{12} = \frac{\pi}{12}$$

So \(z_1 z_2 = 2\sqrt2\, e^{i\pi/12}\).

**Step 3 — Divide moduli, subtract arguments.**

$$\left|\frac{z_1}{z_2}\right| = \frac{\sqrt2}{2} = \frac{\sqrt2}{2}$$

$$\arg\left(\frac{z_1}{z_2}\right) = \frac{\pi}{4} - \left(-\frac{\pi}{6}\right) = \frac{3\pi}{12} + \frac{2\pi}{12} = \frac{5\pi}{12}$$

So \(\dfrac{z_1}{z_2} = \dfrac{\sqrt2}{2}\, e^{i5\pi/12}\).

**Step 4 — Check by direct Cartesian multiplication.**

\(z_1 z_2 = (1+i)(\sqrt3 - i) = (\sqrt3 + 1) + (\sqrt3 - 1)i\).

$$|z_1z_2|^2 = (\sqrt3+1)^2 + (\sqrt3-1)^2 = (4 + 2\sqrt3) + (4 - 2\sqrt3) = 8 \;\Rightarrow\; |z_1z_2| = 2\sqrt2 \; \checkmark$$

Using \(\tan(\pi/12) = 2 - \sqrt3\) (standard value), the ratio \(\dfrac{\sqrt3-1}{\sqrt3+1} = 2-\sqrt3\) confirms \(\arg(z_1z_2) = \pi/12\). ✓

**Common mistake:** subtracting the arguments in the wrong order, or forgetting that \(\arg(z_2)\) is negative here (since \(z_2\) is in the fourth quadrant), which flips the sign of the result for the quotient.

## Answer

\(z_1 z_2 = 2\sqrt2\, e^{i\pi/12}\), \(\;\dfrac{z_1}{z_2} = \dfrac{\sqrt2}{2}\, e^{i5\pi/12}\).
