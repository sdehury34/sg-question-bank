---
title: Finding probabilities and a percentile using the normal distribution
subject: h2-math
topic: Normal Distribution
level: A-Level
difficulty: Medium
description: Standardise a normal random variable to find a probability between two values and the height exceeded by only 10% of a population.
date: 2026-07-19
---

## Question

The heights, \(X\) cm, of adult males in a population are modelled by \( X \sim N(172, 6^2) \).

(a) Find \( P(165 < X < 180) \).

(b) Find the height \(h\), in cm, that is exceeded by only 10% of the population, i.e. find \(h\) such that \(P(X > h) = 0.10\).

## Solution

**Part (a).**

Standardise using \( Z = \dfrac{X - \mu}{\sigma} \) with \( \mu = 172, \sigma = 6 \):

$$z_1 = \frac{165 - 172}{6} = -1.1\overline{6}, \qquad z_2 = \frac{180 - 172}{6} = 1.3\overline{3}$$

$$P(165 < X < 180) = P(z_1 < Z < z_2) = \Phi(1.333) - \Phi(-1.167)$$

Using the standard normal cumulative distribution function, \( \Phi(1.333) = 0.9088 \) and \( \Phi(-1.167) = 1 - \Phi(1.167) = 1 - 0.8784 = 0.1216 \):

$$P(165 < X < 180) = 0.9088 - 0.1216 = 0.7871$$

**Part (b).**

We need \( P(X > h) = 0.10 \), i.e. \( P(X \le h) = 0.90 \), so \( \Phi(z) = 0.90 \) where \( z = \dfrac{h - 172}{6} \).

From the standard normal distribution, \( z = 1.2816 \) (the value satisfying \(\Phi(z) = 0.90\)).

$$h = 172 + 1.2816 \times 6 = 172 + 7.6893 = 179.69$$

**Check.** Substituting \(h = 179.7\) back: \( z = (179.7-172)/6 = 1.2833 \), and \( \Phi(1.2833) \approx 0.9002 \), close to 0.90 (the small discrepancy is rounding of \(z\) to 4 s.f.), confirming the value. Also, since \(h = 179.7\) lies just above the upper bound of part (a)'s interval (180 is very close), it is consistent that only about 10% of the population lies above it, while roughly 78.7% lies between 165 and 180 cm.

**Common mistake:** using \( \Phi(z) = 0.10 \) instead of \( \Phi(z) = 0.90 \) when finding \(h\) — since "exceeded by only 10%" means the **upper** tail is 0.10, so the cumulative probability up to \(h\) must be 0.90, not 0.10. Using the wrong tail gives a value of \(h\) below the mean instead of above it.

## Answer

(a) \( P(165 < X < 180) = 0.787 \) (3 s.f.)

(b) \( h = 179.7 \) cm (3 s.f.)
