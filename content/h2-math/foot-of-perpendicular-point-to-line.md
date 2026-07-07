---
title: Finding the foot of perpendicular from a point to a line in vector form
subject: h2-math
topic: Vectors
level: A-Level
difficulty: Medium
description: Find the foot of perpendicular from a point A to a line l given in vector form, and the shortest distance from A to l.
date: 2026-07-08
---

## Question

The line \(l\) has vector equation \(\mathbf{r} = \begin{pmatrix}1\\0\\2\end{pmatrix} + t\begin{pmatrix}1\\2\\-2\end{pmatrix}\), \(t \in \mathbb{R}\).

The point \(A\) has position vector \(\begin{pmatrix}2\\5\\3\end{pmatrix}\).

Find the position vector of the foot of perpendicular \(N\) from \(A\) to \(l\), and hence find the shortest distance from \(A\) to \(l\).

## Solution

**Step 1 — Write a general point on \(l\).**

$$P(t) = \begin{pmatrix}1\\0\\2\end{pmatrix} + t\begin{pmatrix}1\\2\\-2\end{pmatrix} = \begin{pmatrix}1+t\\2t\\2-2t\end{pmatrix}$$

**Step 2 — Form \(\overrightarrow{AP}\) and use perpendicularity.**

$$\overrightarrow{AP} = P(t) - A = \begin{pmatrix}1+t-2\\2t-5\\2-2t-3\end{pmatrix} = \begin{pmatrix}t-1\\2t-5\\-2t-1\end{pmatrix}$$

At the foot of perpendicular \(N\), \(\overrightarrow{AN}\) is perpendicular to the direction vector \(\mathbf{d} = \begin{pmatrix}1\\2\\-2\end{pmatrix}\), so \(\overrightarrow{AP}\cdot\mathbf{d} = 0\):

$$1(t-1) + 2(2t-5) + (-2)(-2t-1) = 0$$
$$(t-1) + (4t-10) + (4t+2) = 0$$
$$9t - 9 = 0 \quad\Rightarrow\quad t = 1$$

**Step 3 — Find \(N\).**

$$N = P(1) = \begin{pmatrix}1+1\\2(1)\\2-2(1)\end{pmatrix} = \begin{pmatrix}2\\2\\0\end{pmatrix}$$

**Step 4 — Find the shortest distance \(|AN|\).**

$$\overrightarrow{AN} = N - A = \begin{pmatrix}0\\-3\\-3\end{pmatrix}$$
$$|AN| = \sqrt{0^2 + (-3)^2 + (-3)^2} = \sqrt{18} = 3\sqrt{2}$$

**Check (alternative method):** using \(\overrightarrow{AP}(0) = \begin{pmatrix}-1\\-5\\-1\end{pmatrix}\) (taking \(t=0\)), the perpendicular distance formula gives

$$\text{distance} = \frac{|\overrightarrow{AP}(0) \times \mathbf{d}|}{|\mathbf{d}|} = \frac{|(12,-3,3)|}{\sqrt{1+4+4}} = \frac{\sqrt{144+9+9}}{3} = \frac{\sqrt{162}}{3} = \frac{9\sqrt{2}}{3} = 3\sqrt{2}$$

This matches Step 4, confirming the answer.

**Common mistake:** setting \(\overrightarrow{AP}\cdot\mathbf{d} = 0\) using \(\overrightarrow{PA}\) instead of \(\overrightarrow{AP}\) (a sign slip that doesn't affect this particular dot product equation, but frequently causes errors when students then reuse the vector's direction elsewhere) — and, more seriously, forgetting to substitute the solved \(t\) back into \(P(t)\) to actually state \(N\), leaving the answer as just a value of \(t\).

## Answer

The foot of perpendicular is \(N = \begin{pmatrix}2\\2\\0\end{pmatrix}\), and the shortest distance from \(A\) to \(l\) is \(3\sqrt{2} \approx 4.24\) units (3 s.f.).
