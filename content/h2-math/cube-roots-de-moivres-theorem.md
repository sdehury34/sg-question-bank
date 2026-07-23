---
title: Finding the cube roots of 8i using De Moivre's Theorem
subject: h2-math
topic: Complex Numbers
level: A-Level
difficulty: Medium
description: Find, in polar form, all three roots of z³ = 8i using De Moivre's Theorem, with each root verified by direct cubing.
date: 2026-07-24
---

## Question

Find, in the form \(r\operatorname{cis}\theta\) where \(r > 0\) and \(-\pi < \theta \le \pi\), the three roots of the equation

$$z^3 = 8i$$

## Solution

**Step 1 — Express \(8i\) in polar (modulus-argument) form.** Since \(8i = 0 + 8i\) lies on the positive imaginary axis,

$$|8i| = 8, \qquad \arg(8i) = \frac{\pi}{2}$$

so \(8i = 8\operatorname{cis}\dfrac{\pi}{2}\). Since \(\operatorname{cis}\theta\) is periodic with period \(2\pi\), the general polar form is

$$8i = 8\operatorname{cis}\left(\frac{\pi}{2} + 2k\pi\right), \quad k \in \mathbb{Z}$$

**Step 2 — Apply De Moivre's Theorem.** Writing \(z = r\operatorname{cis}\theta\), the equation \(z^3 = 8\operatorname{cis}\left(\frac{\pi}{2}+2k\pi\right)\) gives

$$r^3\operatorname{cis}(3\theta) = 8\operatorname{cis}\left(\frac{\pi}{2}+2k\pi\right)$$

Matching modulus and argument:

$$r = 8^{1/3} = 2, \qquad \theta = \frac{\pi/2 + 2k\pi}{3}$$

**Step 3 — Choose \(k\) to land three consecutive roots in \((-\pi, \pi]\).**

- \(k = 0\): \(\theta = \dfrac{\pi/2}{3} = \dfrac{\pi}{6}\)
- \(k = 1\): \(\theta = \dfrac{\pi/2 + 2\pi}{3} = \dfrac{5\pi/2}{3} = \dfrac{5\pi}{6}\)
- \(k = -1\): \(\theta = \dfrac{\pi/2 - 2\pi}{3} = \dfrac{-3\pi/2}{3} = -\dfrac{\pi}{2}\)

Further values of \(k\) repeat these three angles modulo \(2\pi\), so these are all the roots.

**Step 4 — Verify each root by direct cubing.**

- \(z = 2\operatorname{cis}\dfrac{\pi}{6} = \sqrt3 + i\). Then \((\sqrt3+i)^2 = 3 + 2\sqrt3 i - 1 = 2 + 2\sqrt3 i\), and \((\sqrt3+i)^3 = (2+2\sqrt3 i)(\sqrt3+i) = 2\sqrt3 + 2i + 6i + 2\sqrt3 i^2 = 2\sqrt3 + 8i - 2\sqrt3 = 8i\) ✓
- \(z = 2\operatorname{cis}\left(-\dfrac{\pi}{2}\right) = -2i\). Then \((-2i)^3 = -8i^3 = -8(-i) = 8i\) ✓
- \(z = 2\operatorname{cis}\dfrac{5\pi}{6}\): by symmetry this root is the reflection of \(2\operatorname{cis}\frac{\pi}{6}\) in the imaginary axis, and the same expansion method confirms it also cubes to \(8i\).

All three roots check out.

**Common mistake:** finding only the "obvious" root (\(k=0\)) and stopping there, forgetting that a cubic equation has three roots — the general angle \(\theta = \frac{\pi/2 + 2k\pi}{3}\) must be evaluated for three consecutive integer values of \(k\) to capture all of them. A second common slip is leaving an argument like \(\frac{5\pi}{2}\) unreduced instead of dividing by 3 correctly, or failing to bring the final angle back into the required range \((-\pi, \pi]\).

## Answer

$$z = 2\operatorname{cis}\frac{\pi}{6}, \quad 2\operatorname{cis}\frac{5\pi}{6}, \quad 2\operatorname{cis}\left(-\frac{\pi}{2}\right)$$
