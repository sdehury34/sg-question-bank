---
title: Finding the angle between two vectors and the area they enclose
subject: h2-math
topic: Vectors
level: A-Level
difficulty: Medium
description: Use the scalar and vector products to find the angle between two 3D vectors and the area of the parallelogram they form.
date: 2026-07-22
---

## Question

Vectors \(\mathbf{a}\) and \(\mathbf{b}\) are given by

$$\mathbf{a} = 2\mathbf{i} + 2\mathbf{j} - \mathbf{k}, \qquad \mathbf{b} = 6\mathbf{i} - 3\mathbf{j} + 2\mathbf{k}$$

(a) Find the angle between \(\mathbf{a}\) and \(\mathbf{b}\), giving your answer in degrees to 3 s.f.

(b) Hence find the area of the parallelogram with adjacent sides \(\mathbf{a}\) and \(\mathbf{b}\).

## Solution

**Part (a) — angle via the scalar (dot) product.**

$$\mathbf{a} \cdot \mathbf{b} = (2)(6) + (2)(-3) + (-1)(2) = 12 - 6 - 2 = 4$$

$$|\mathbf{a}| = \sqrt{2^2 + 2^2 + (-1)^2} = \sqrt{9} = 3, \qquad |\mathbf{b}| = \sqrt{6^2 + (-3)^2 + 2^2} = \sqrt{49} = 7$$

Using \(\mathbf{a}\cdot\mathbf{b} = |\mathbf{a}||\mathbf{b}|\cos\theta\):

$$\cos\theta = \frac{4}{3 \times 7} = \frac{4}{21}$$

$$\theta = \cos^{-1}\left(\frac{4}{21}\right) = 79.0° \ (\text{3 s.f.})$$

**Part (b) — area via the vector (cross) product.**

$$\mathbf{a} \times \mathbf{b} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 2 & 2 & -1 \\ 6 & -3 & 2 \end{vmatrix}
= \mathbf{i}\big[(2)(2)-(-1)(-3)\big] - \mathbf{j}\big[(2)(2)-(-1)(6)\big] + \mathbf{k}\big[(2)(-3)-(2)(6)\big]$$

$$= \mathbf{i}(4-3) - \mathbf{j}(4+6) + \mathbf{k}(-6-12) = \mathbf{i} - 10\mathbf{j} - 18\mathbf{k}$$

$$|\mathbf{a}\times\mathbf{b}| = \sqrt{1^2 + (-10)^2 + (-18)^2} = \sqrt{1+100+324} = \sqrt{425} = 20.6 \ (\text{3 s.f.})$$

The area of the parallelogram equals \(|\mathbf{a}\times\mathbf{b}|\), so the area is \(20.6\) square units.

**Check.** The area should also equal \(|\mathbf{a}||\mathbf{b}|\sin\theta\):

$$3 \times 7 \times \sin(79.019°) = 21 \times 0.98169 = 20.6$$

This matches the cross-product result, confirming both parts.

**Common mistake:** using \(\sin\theta\) together with the *dot* product formula (or \(\cos\theta\) with the cross product) — the dot product gives \(\cos\theta\) and the cross product's magnitude gives \(|\mathbf{a}||\mathbf{b}|\sin\theta\); mixing them up gives a nonsensical area or angle.

## Answer

(a) \(\theta = 79.0°\) (3 s.f.)

(b) Area \(= \sqrt{425} = 20.6\) square units (3 s.f.)
