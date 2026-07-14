---
title: Poisson distribution — probability of more than 4 calls in 5 minutes
subject: h2-math
topic: The Poisson Distribution
level: A-Level
difficulty: Medium
description: Model calls arriving at a telephone exchange with a Poisson distribution and find the probability of receiving more than 4 calls in a 5-minute interval.
date: 2026-07-15
---

## Question

Calls arrive at a telephone exchange randomly and independently at an average rate of 3 calls per 5-minute interval. Find the probability that, in a randomly chosen 5-minute interval, the exchange receives more than 4 calls. Give your answer correct to 3 significant figures.

## Solution

**Step 1 — Set up the model.** Calls occur randomly, independently, and at a constant average rate, so the number of calls \(X\) in a 5-minute interval can be modelled by

$$X \sim \text{Po}(3)$$

since the mean number of calls per 5-minute interval is \(\lambda = 3\).

**Step 2 — Identify what is required.** We want \(P(X > 4) = 1 - P(X \le 4)\).

**Step 3 — Compute \(P(X \le 4)\)** using \(P(X = k) = \dfrac{e^{-\lambda}\lambda^k}{k!}\) with \(\lambda = 3\):

$$P(X=0) = e^{-3} = 0.049787$$
$$P(X=1) = e^{-3}(3) = 0.149361$$
$$P(X=2) = e^{-3}\frac{3^2}{2!} = 0.224042$$
$$P(X=3) = e^{-3}\frac{3^3}{3!} = 0.224042$$
$$P(X=4) = e^{-3}\frac{3^4}{4!} = 0.168031$$

Summing:

$$P(X \le 4) = 0.049787 + 0.149361 + 0.224042 + 0.224042 + 0.168031 = 0.815263$$

**Step 4 — Complement.**

$$P(X > 4) = 1 - 0.815263 = 0.184737$$

**Step 5 — Check.** This was verified numerically (summing the five Poisson terms with \(\lambda = 3\) directly and subtracting from 1 gives 0.184737, matching the hand computation above), and the value is sensible: since the mean is 3, receiving more than 4 (i.e. at least 5) is somewhat unlikely but not negligible, consistent with a probability of about 0.185.

**Common mistake:** computing \(P(X > 4)\) as \(1 - P(X \le 5)\) or \(1 - P(X < 4)\) — "more than 4" means \(X \ge 5\), so the complement must be taken against \(P(X \le 4)\), not \(P(X \le 5)\) or \(P(X \le 3)\).

## Answer

$$P(X > 4) = 0.185 \text{ (3 s.f.)}$$
