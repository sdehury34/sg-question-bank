---
title: Probability of drawing two balls of different colours without replacement
subject: emath
topic: Probability of Combined Events
level: O-Level
difficulty: Medium
description: Use a tree diagram approach to find the probability that two balls drawn without replacement from a bag are different colours.
date: 2026-07-14
---

## Question

A bag contains 5 red balls and 3 blue balls. Two balls are drawn at random from the bag, one after another, **without replacement**. Find the probability that the two balls drawn are of different colours.

## Solution

**Step 1 — Set up the probabilities for the first draw.** There are \(5 + 3 = 8\) balls in total.

$$P(\text{Red}_1) = \frac{5}{8} \qquad P(\text{Blue}_1) = \frac{3}{8}$$

**Step 2 — Set up the probabilities for the second draw.** Since the first ball is not replaced, only 7 balls remain, and the counts depend on what was drawn first.

If the first ball was red (4 red, 3 blue left):

$$P(\text{Blue}_2 \mid \text{Red}_1) = \frac{3}{7}$$

If the first ball was blue (5 red, 2 blue left):

$$P(\text{Red}_2 \mid \text{Blue}_1) = \frac{5}{7}$$

**Step 3 — "Different colours" means Red-then-Blue OR Blue-then-Red.** These two outcomes are mutually exclusive, so add their probabilities.

$$P(R_1, B_2) = \frac{5}{8} \times \frac{3}{7} = \frac{15}{56}$$

$$P(B_1, R_2) = \frac{3}{8} \times \frac{5}{7} = \frac{15}{56}$$

$$P(\text{different colours}) = \frac{15}{56} + \frac{15}{56} = \frac{30}{56} = \frac{15}{28}$$

**Step 4 — Check using the complement.** \(P(\text{same colour}) = P(R_1,R_2) + P(B_1,B_2)\).

$$P(R_1, R_2) = \frac{5}{8} \times \frac{4}{7} = \frac{20}{56} \qquad P(B_1, B_2) = \frac{3}{8} \times \frac{2}{7} = \frac{6}{56}$$

$$P(\text{same colour}) = \frac{20}{56} + \frac{6}{56} = \frac{26}{56} = \frac{13}{28}$$

$$P(\text{different colours}) = 1 - \frac{13}{28} = \frac{15}{28}$$

This matches Step 3 exactly, confirming the answer.

**Common mistake:** using \(\dfrac{3}{8}\) instead of \(\dfrac{3}{7}\) for the second draw (forgetting that "without replacement" reduces the total to 7), or only calculating \(P(R_1, B_2)\) and forgetting to also add \(P(B_1, R_2)\) — "different colours" can happen in either order.

## Answer

$$P(\text{different colours}) = \frac{15}{28}$$
