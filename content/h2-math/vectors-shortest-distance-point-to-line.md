---
title: Shortest distance from a point to a line in vector form
subject: h2-math
topic: Vectors
level: A-Level
difficulty: Medium
description: Find the perpendicular distance from a given point to a line given in vector equation form, using the cross product method.
date: 2026-07-16
---

## Question

The line \(l\) has vector equation
$$\mathbf{r} = \begin{pmatrix}1\\2\\-1\end{pmatrix} + t\begin{pmatrix}2\\-1\\2\end{pmatrix}, \quad t \in \mathbb{R}.$$

Find the shortest distance from the point \(A(3, 0, 4)\) to the line \(l\), giving your answer correct to 3 significant figures.

## Solution

**Setting up the vectors.** Let \(P_0 = (1, 2, -1)\) be the point on \(l\) given by \(t=0\), with direction vector \(\mathbf{d} = \begin{pmatrix}2\\-1\\2\end{pmatrix}\), so \(|\mathbf{d}| = \sqrt{4+1+4} = 3\).

The vector from \(P_0\) to \(A\) is
$$\overrightarrow{P_0A} = \begin{pmatrix}3-1\\0-2\\4-(-1)\end{pmatrix} = \begin{pmatrix}2\\-2\\5\end{pmatrix}$$

**Using the cross product formula.** The shortest (perpendicular) distance from \(A\) to \(l\) is
$$d = \frac{|\overrightarrow{P_0A} \times \mathbf{d}|}{|\mathbf{d}|}$$

Computing the cross product:
$$\overrightarrow{P_0A} \times \mathbf{d} = \begin{pmatrix}2\\-2\\5\end{pmatrix} \times \begin{pmatrix}2\\-1\\2\end{pmatrix} = \begin{pmatrix}(-2)(2)-(5)(-1)\\(5)(2)-(2)(2)\\(2)(-1)-(-2)(2)\end{pmatrix} = \begin{pmatrix}1\\6\\2\end{pmatrix}$$

So \(|\overrightarrow{P_0A} \times \mathbf{d}| = \sqrt{1^2+6^2+2^2} = \sqrt{41}\), and
$$d = \frac{\sqrt{41}}{3} = 2.1344\ldots \approx 2.13$$

**Check by finding the foot of perpendicular directly.** A general point on \(l\) is \(N = (1+2t,\ 2-t,\ -1+2t)\). Then \(\overrightarrow{AN} = (2t-2,\ 2-t,\ 2t-5)\). Since \(\overrightarrow{AN} \perp \mathbf{d}\):
$$2(2t-2) - (2-t) + 2(2t-5) = 0 \implies 9t - 16 = 0 \implies t = \tfrac{16}{9}$$

This gives \(N = \left(\tfrac{41}{9}, \tfrac{2}{9}, \tfrac{23}{9}\right)\), and
$$\overrightarrow{AN} = A - N = \left(-\tfrac{14}{9}, -\tfrac{2}{9}, \tfrac{13}{9}\right), \quad |\overrightarrow{AN}| = \frac{\sqrt{196+4+169}}{9} = \frac{\sqrt{369}}{9} = \frac{3\sqrt{41}}{9} = \frac{\sqrt{41}}{3}$$

This matches the cross-product result exactly, confirming \(d = \dfrac{\sqrt{41}}{3} \approx 2.13\).

**Common mistake:** dividing by \(|\overrightarrow{P_0A}|\) instead of \(|\mathbf{d}|\) in the distance formula, or forgetting to take the magnitude of the cross product before dividing — both give a numerically wrong distance even though the cross product itself was computed correctly.

## Answer

The shortest distance from \(A\) to \(l\) is \(\dfrac{\sqrt{41}}{3} \approx\) **2.13 units** (3 s.f.).
