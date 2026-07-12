---
title: Expressing (1 + i√3)⁶ in the form a + bi using De Moivre's Theorem
subject: h2-math
topic: Complex Numbers
level: A-Level
difficulty: Medium
description: Use De Moivre's Theorem to evaluate (1 + i√3)⁶ by converting to modulus-argument form first.
date: 2026-07-13
---

## Question

Express \((1 + i\sqrt{3})^6\) in the form \(a + bi\), using De Moivre's Theorem.

## Solution

**Step 1 — Convert \(1 + i\sqrt{3}\) to modulus-argument form.**

$$|1 + i\sqrt{3}| = \sqrt{1^2 + (\sqrt{3})^2} = \sqrt{4} = 2$$

$$\arg(1 + i\sqrt{3}) = \tan^{-1}\left(\frac{\sqrt{3}}{1}\right) = 60^\circ$$

(The point \(1 + i\sqrt3\) lies in the first quadrant, so the argument is exactly this reference angle.)

$$1 + i\sqrt{3} = 2(\cos 60^\circ + i \sin 60^\circ)$$

**Step 2 — Apply De Moivre's Theorem.**

$$(1+i\sqrt3)^6 = 2^6(\cos(6 \times 60^\circ) + i\sin(6\times 60^\circ)) = 64(\cos 360^\circ + i \sin 360^\circ)$$

**Step 3 — Simplify.** Since \(\cos 360^\circ = 1\) and \(\sin 360^\circ = 0\):

$$(1+i\sqrt3)^6 = 64(1 + 0i) = 64$$

**Step 4 — Check by direct expansion.**

$$(1+i\sqrt3)^2 = 1 + 2i\sqrt3 + 3i^2 = 1 + 2i\sqrt3 - 3 = -2 + 2i\sqrt3$$

$$(1+i\sqrt3)^4 = (-2+2i\sqrt3)^2 = 4 - 8i\sqrt3 + 4(3)i^2 = 4 - 8i\sqrt3 - 12 = -8 - 8i\sqrt3$$

$$(1+i\sqrt3)^6 = (1+i\sqrt3)^4 (1+i\sqrt3)^2 = (-8-8i\sqrt3)(-2+2i\sqrt3)$$

$$= 16 - 16i\sqrt3 + 16i\sqrt3 - 16(3)i^2 = 16 + 48 = 64$$

This matches the De Moivre's Theorem result, confirming the answer.

**Common mistake:** after multiplying the argument by 6 to get \(360^\circ\), forgetting that this wraps back to \(0^\circ\) and leaving the answer as "\(64 \operatorname{cis} 360^\circ\)" instead of simplifying \(\cos 360^\circ = 1\), \(\sin 360^\circ = 0\) to the real number \(64\).

## Answer

\((1 + i\sqrt{3})^6 = 64\)
