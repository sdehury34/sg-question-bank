---
title: Using the cosine rule to find a side of a non-right-angled triangle
subject: emath
topic: Trigonometry
level: O-Level
difficulty: Medium
description: Apply the cosine rule to find side BC in triangle ABC given AB = 7 cm, AC = 9 cm and angle BAC = 65 degrees.
date: 2026-07-07
---

## Question

In triangle ABC, \(AB = 7\) cm, \(AC = 9\) cm and \(\angle BAC = 65°\). Find the length of \(BC\), giving your answer correct to 3 significant figures.

## Solution

Two sides and the **included** angle are given, so the cosine rule applies:

$$BC^2 = AB^2 + AC^2 - 2 \cdot AB \cdot AC \cdot \cos(\angle BAC)$$

Substituting the values:

$$BC^2 = 7^2 + 9^2 - 2 \times 7 \times 9 \times \cos 65°$$

$$BC^2 = 49 + 81 - 126 \times 0.42262$$

$$BC^2 = 130 - 53.250 = 76.750$$

$$BC = \sqrt{76.750} = 8.7607\ldots \approx 8.76 \text{ cm}$$

**Check:** substituting \(BC = 8.7607\) back, \(BC^2 = 76.75\), and \(49 + 81 - 126\cos 65° = 130 - 53.250 = 76.75\) — the two sides of the cosine rule agree, confirming the answer.

**Common mistake:** reaching for the **sine rule** because two sides and an angle are known. The sine rule needs a side and its *opposite* angle as a matching pair — here only the angle *between* the two given sides is known, so the cosine rule must be used instead. A related mistake is dropping the \(-2 \cdot AB \cdot AC \cos(\angle BAC)\) term entirely and just adding the squares (as in Pythagoras' theorem), which only holds when the included angle is 90°.

## Answer

\(BC \approx 8.76\) cm (3 s.f.)
