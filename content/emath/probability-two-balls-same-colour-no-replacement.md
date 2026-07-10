---
title: Probability both balls drawn are the same colour without replacement
subject: emath
topic: Probability
level: O-Level
difficulty: Medium
description: Find the probability that two balls drawn without replacement from a bag are the same colour, using a tree diagram approach.
date: 2026-07-11
---

## Question

A bag contains 5 red balls and 3 blue balls. Two balls are drawn from the bag at random, one after another, **without replacement**. Find the probability that both balls drawn are the same colour.

## Solution

**Step 1 — Set up the two ways of getting "same colour".** Both balls are the same colour if either both are red (RR) or both are blue (BB). These two outcomes are mutually exclusive, so

$$P(\text{same colour}) = P(RR) + P(BB)$$

**Step 2 — Find \(P(RR)\).** There are 8 balls in total to start. For the first draw, \(P(\text{red}) = \frac{5}{8}\). Since the ball is not replaced, only 7 balls remain (4 of them red) for the second draw:

$$P(RR) = \frac{5}{8} \times \frac{4}{7} = \frac{20}{56} = \frac{5}{14}$$

**Step 3 — Find \(P(BB)\).** For the first draw, \(P(\text{blue}) = \frac{3}{8}\). After removing one blue ball, 7 balls remain (2 of them blue):

$$P(BB) = \frac{3}{8} \times \frac{2}{7} = \frac{6}{56} = \frac{3}{28}$$

**Step 4 — Add the two probabilities**, using a common denominator of 28:

$$P(\text{same colour}) = \frac{5}{14} + \frac{3}{28} = \frac{10}{28} + \frac{3}{28} = \frac{13}{28}$$

**Check — all four branch probabilities sum to 1.** The remaining two outcomes are "red then blue" (RB) and "blue then red" (BR):

$$P(RB) = \frac{5}{8} \times \frac{3}{7} = \frac{15}{56}, \qquad P(BR) = \frac{3}{8} \times \frac{5}{7} = \frac{15}{56}$$

$$P(RR)+P(BB)+P(RB)+P(BR) = \frac{20}{56}+\frac{6}{56}+\frac{15}{56}+\frac{15}{56} = \frac{56}{56} = 1 \checkmark$$

Since all four mutually exclusive outcomes correctly sum to 1, the value of \(P(\text{same colour}) = \frac{13}{28}\) is confirmed.

**Common mistake:** using \(\frac{5}{8}\times\frac{4}{8}\) (or \(\frac{3}{8}\times\frac{3}{8}\)) for the second draw — i.e. forgetting that "without replacement" reduces **both** the numerator (one fewer ball of that colour) **and** the denominator (one fewer ball overall) on the second draw. The denominator for the second draw must be 7, not 8.

## Answer

\(P(\text{same colour}) = \dfrac{13}{28}\) (≈ 0.464).
