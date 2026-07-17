---
title: Using De Moivre's Theorem to evaluate (1 + i√3)^6
subject: h2-math
topic: Complex Numbers
level: A-Level
difficulty: Medium
description: Express 1 + i√3 in modulus-argument form and use De Moivre's Theorem to find (1 + i√3)^6 in the form a + bi.
date: 2026-07-18
---

## Question

Let \(z = 1 + i\sqrt{3}\).

(a) Express \(z\) in the form \(r(\cos\theta + i\sin\theta)\), where \(r > 0\) and \(-\pi < \theta \le \pi\).

(b) Hence use De Moivre's Theorem to find \(z^{6}\) in the form \(a + bi\).

(c) State \(|z^{6}|\) and \(\arg(z^6)\).

## Solution

**Part (a) — modulus-argument form.**

$$r = |z| = \sqrt{1^{2} + (\sqrt{3})^{2}} = \sqrt{1+3} = 2$$

Since the real part is 1 and the imaginary part is \(\sqrt3\) (both positive, so \(z\) lies in the first quadrant),

$$\theta = \arg(z) = \arctan\!\left(\frac{\sqrt3}{1}\right) = \frac{\pi}{3}$$

So

$$z = 2\left(\cos\frac{\pi}{3} + i\sin\frac{\pi}{3}\right)$$

**Part (b) — De Moivre's Theorem.** For \(z^n = r^n(\cos n\theta + i \sin n\theta)\), with \(n=6\):

$$z^{6} = 2^{6}\left(\cos\frac{6\pi}{3} + i\sin\frac{6\pi}{3}\right) = 64\left(\cos 2\pi + i \sin 2\pi\right)$$

Since \(\cos 2\pi = 1\) and \(\sin 2\pi = 0\):

$$z^{6} = 64(1 + 0i) = 64$$

**Part (c).** \(z^6 = 64\) is a positive real number, so

$$|z^6| = 64, \qquad \arg(z^6) = 0$$

**Check by direct binomial expansion (verified by computer algebra):** expanding \((1+i\sqrt3)^6\) directly and simplifying using \(i^2 = -1\) also gives exactly \(64 + 0i\), confirming the De Moivre result.

**Common mistake:** stopping at \(\arg(z^6) = 2\pi\) instead of reducing it to the principal value \(0\) (since \(-\pi < \arg z \le \pi\) is required). Another common slip is writing \(\theta = \arctan(\sqrt3)\) without checking the quadrant — it happens to be correct here since \(z\) is in the first quadrant, but the same mistake gives a wrong angle whenever the real part is negative.

## Answer

(a) \(z = 2\left(\cos\dfrac{\pi}{3} + i\sin\dfrac{\pi}{3}\right)\)

(b) \(z^{6} = 64\)

(c) \(|z^6| = 64\), \(\arg(z^6) = 0\)
