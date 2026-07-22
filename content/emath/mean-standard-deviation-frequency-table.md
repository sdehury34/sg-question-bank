---
title: Finding mean and standard deviation from a frequency table
subject: emath
topic: Statistics
level: O-Level
difficulty: Medium
description: Calculate the mean and standard deviation of the number of goals scored per match from a discrete frequency table of 20 matches.
date: 2026-07-23
---

## Question

The table shows the number of goals scored by a football team in each of 20 matches.

- Goals scored, \(x = 0\): frequency \(f = 3\)
- Goals scored, \(x = 1\): frequency \(f = 6\)
- Goals scored, \(x = 2\): frequency \(f = 5\)
- Goals scored, \(x = 3\): frequency \(f = 4\)
- Goals scored, \(x = 4\): frequency \(f = 2\)

Calculate, for this data,

(a) the mean number of goals scored per match,

(b) the standard deviation, giving your answer correct to 3 significant figures.

## Solution

**Step 1 — Check the total frequency.**

$$\sum f = 3+6+5+4+2 = 20$$

This matches the 20 matches stated, confirming no frequency has been missed.

**Step 2 — Find \(\sum fx\) for the mean.**

$$\sum fx = (0)(3)+(1)(6)+(2)(5)+(3)(4)+(4)(2) = 0+6+10+12+8 = 36$$

$$\bar{x} = \frac{\sum fx}{\sum f} = \frac{36}{20} = 1.8$$

**Step 3 — Find \(\sum fx^2\) for the standard deviation.**

$$\sum fx^2 = (0^2)(3)+(1^2)(6)+(2^2)(5)+(3^2)(4)+(4^2)(2) = 0+6+20+36+32 = 94$$

**Step 4 — Apply the standard deviation formula.**

$$\sigma = \sqrt{\frac{\sum fx^2}{\sum f} - \bar{x}^2} = \sqrt{\frac{94}{20} - 1.8^2} = \sqrt{4.7 - 3.24} = \sqrt{1.46}$$

$$\sigma = 1.2083\ldots \approx 1.21 \ (3\text{ s.f.})$$

**Check:** since the goals range from 0 to 4 with most matches clustered around 1–2 goals, a standard deviation of about 1.21 goals is a reasonable spread — not implausibly large or small relative to the mean of 1.8.

**Common mistake:** dividing \(\sum fx^2\) and \(\bar{x}^2\) by the number of categories (5) instead of the total frequency \(\sum f = 20\), or computing \(\bar{x}^2\) before subtracting instead of subtracting first — both errors are avoided by carefully following \(\sigma = \sqrt{\frac{\sum fx^2}{\sum f} - \bar{x}^2}\) term by term.

## Answer

Mean \(= 1.8\) goals per match.
Standard deviation \(= 1.21\) goals per match (3 s.f.).
