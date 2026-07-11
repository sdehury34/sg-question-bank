---
title: Shortest distance from a point to a line in vector form
subject: h2-math
topic: Vectors
level: A-Level
difficulty: Medium
description: Step-by-step vector method for finding the shortest distance from a point to a line using the cross product formula, checked against a foot-of-perpendicular calculation.
date: 2026-07-12
---

## Question

The line \( l \) has vector equation

$$\mathbf{r} = \begin{pmatrix}1\\2\\3\end{pmatrix} + \lambda\begin{pmatrix}2\\-1\\2\end{pmatrix}, \quad \lambda \in \mathbb{R}$$

Find the shortest distance from the point \( A(4, 0, 1) \) to the line \( l \), giving your answer correct to 3 significant figures.

## Solution

Let \( P_0 = (1,2,3) \) be the known point on \( l \), with direction vector \( \mathbf{d} = \begin{pmatrix}2\\-1\\2\end{pmatrix} \), so \( |\mathbf{d}| = \sqrt{4+1+4} = 3 \).

The vector from \( P_0 \) to \( A \) is

$$\overrightarrow{P_0A} = \begin{pmatrix}4-1\\0-2\\1-3\end{pmatrix} = \begin{pmatrix}3\\-2\\-2\end{pmatrix}$$

The shortest (perpendicular) distance from \( A \) to \( l \) is given by

$$d = \frac{\left|\overrightarrow{P_0A} \times \mathbf{d}\right|}{|\mathbf{d}|}$$

Compute the cross product:

$$\overrightarrow{P_0A} \times \mathbf{d} = \begin{pmatrix}3\\-2\\-2\end{pmatrix} \times \begin{pmatrix}2\\-1\\2\end{pmatrix} = \begin{pmatrix}(-2)(2)-(-2)(-1)\\(-2)(2)-(3)(2)\\(3)(-1)-(-2)(2)\end{pmatrix} = \begin{pmatrix}-6\\-10\\1\end{pmatrix}$$

$$\left|\overrightarrow{P_0A} \times \mathbf{d}\right| = \sqrt{(-6)^2 + (-10)^2 + 1^2} = \sqrt{137}$$

$$d = \frac{\sqrt{137}}{3} \approx 3.90 \text{ (3 s.f.)}$$

**Check by finding the foot of perpendicular.** The parameter at the foot \( F \) is \( t = \dfrac{\overrightarrow{P_0A}\cdot\mathbf{d}}{\mathbf{d}\cdot\mathbf{d}} = \dfrac{(3)(2)+(-2)(-1)+(-2)(2)}{9} = \dfrac{4}{9} \).

$$F = \begin{pmatrix}1\\2\\3\end{pmatrix} + \frac{4}{9}\begin{pmatrix}2\\-1\\2\end{pmatrix} = \begin{pmatrix}17/9\\14/9\\35/9\end{pmatrix}$$

$$\overrightarrow{AF} = \begin{pmatrix}19/9\\-14/9\\-26/9\end{pmatrix}, \qquad |\overrightarrow{AF}| = \frac{\sqrt{19^2+14^2+26^2}}{9} = \frac{\sqrt{1233}}{9} \approx 3.90$$

This agrees with the cross-product result, confirming the answer.

**Common mistake:** Dividing the cross product magnitude by \( |\mathbf{d}|^2 \) instead of \( |\mathbf{d}| \), or leaving the final answer as a vector instead of taking its magnitude to get a scalar distance.

## Answer

Shortest distance \( = \dfrac{\sqrt{137}}{3} \approx 3.90 \) units (3 s.f.)
