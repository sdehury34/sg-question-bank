---
title: Expressing a complex number in polar form and applying De Moivre's theorem
subject: h2-math
topic: Complex Numbers
level: A-Level
difficulty: Medium
description: Convert the complex number root 3 plus i to modulus-argument form and use De Moivre's theorem to evaluate its sixth power exactly.
date: 2026-07-10
---

## Question

The complex number \( z = \sqrt{3} + i \).

(a) Express \(z\) in the form \( r(\cos\theta + i\sin\theta) \), where \( r > 0 \) and \( -\pi < \theta \le \pi \), giving \(r\) and \(\theta\) exactly.

(b) Hence use De Moivre's theorem to find \( z^6 \), giving your answer in the form \( x + iy \).

## Solution

**(a) Polar form**

The modulus is
$$r = |z| = \sqrt{(\sqrt{3})^2 + 1^2} = \sqrt{3+1} = 2$$

Since the real part \( \sqrt{3} > 0 \) and the imaginary part \( 1 > 0 \), \(z\) lies in the first quadrant, so
$$\theta = \arctan\left(\frac{1}{\sqrt{3}}\right) = \frac{\pi}{6}$$

Hence
$$z = 2\left(\cos\frac{\pi}{6} + i\sin\frac{\pi}{6}\right)$$

**(b) Applying De Moivre's theorem**

De Moivre's theorem states \( z^n = r^n(\cos n\theta + i \sin n\theta) \). With \( n = 6 \):
$$z^6 = 2^6\left(\cos\left(6 \times \frac{\pi}{6}\right) + i\sin\left(6 \times \frac{\pi}{6}\right)\right) = 64(\cos\pi + i\sin\pi)$$

Since \( \cos\pi = -1 \) and \( \sin\pi = 0 \):
$$z^6 = 64(-1 + 0i) = -64$$

**Check by direct expansion:** \( z^2 = (\sqrt{3}+i)^2 = 3 + 2\sqrt{3}i - 1 = 2 + 2\sqrt{3}i \).
$$z^3 = z^2 \cdot z = (2+2\sqrt{3}i)(\sqrt{3}+i) = 2\sqrt{3} + 2i + 6i + 2\sqrt{3}i^2 = 2\sqrt{3} + 8i - 2\sqrt{3} = 8i$$

Then \( z^6 = (z^3)^2 = (8i)^2 = 64i^2 = -64 \), which agrees with the polar-form result. ✓

**Common mistake:** Forgetting that De Moivre's theorem raises the *modulus* to the power \(n\) as well — writing \( z^6 = \cos 6\theta + i \sin 6\theta \) (dropping the \( r^6 = 64 \) factor) is a very common slip.

## Answer

\( z = 2\left(\cos\dfrac{\pi}{6} + i\sin\dfrac{\pi}{6}\right) \) and \( z^6 = -64 \).
