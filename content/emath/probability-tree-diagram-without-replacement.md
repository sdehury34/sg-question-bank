---
title: Probability of drawing two balls without replacement from a bag
subject: emath
topic: Probability
level: O-Level
difficulty: Medium
description: Use a tree diagram to find the probability of drawing two red balls, and two different-coloured balls, from a bag without replacement.
date: 2026-07-24
---

## Question

A bag contains 5 red balls and 3 blue balls. Two balls are drawn at random from the bag, one after another, **without replacement**. Find the probability that

(a) both balls are red,

(b) the two balls are of different colours.

## Solution

There are \(5 + 3 = 8\) balls in total at the start.

**Setting up the tree diagram (without replacement).** After the first ball is removed, only 7 balls remain, so the probabilities on the second draw depend on the colour of the first ball drawn:

- 1st draw: \(P(R) = \dfrac{5}{8}\), \(P(B) = \dfrac{3}{8}\)
- 2nd draw given 1st was R: \(P(R) = \dfrac{4}{7}\), \(P(B) = \dfrac{3}{7}\)
- 2nd draw given 1st was B: \(P(R) = \dfrac{5}{7}\), \(P(B) = \dfrac{2}{7}\)

**(a) P(both red).** Multiply along the R–R branch:

$$P(RR) = \frac{5}{8} \times \frac{4}{7} = \frac{20}{56} = \frac{5}{14}$$

**(b) P(different colours).** This happens via two branches — Red-then-Blue **or** Blue-then-Red — so add their probabilities:

$$P(RB) = \frac{5}{8} \times \frac{3}{7} = \frac{15}{56}, \qquad P(BR) = \frac{3}{8} \times \frac{5}{7} = \frac{15}{56}$$

$$P(\text{different}) = \frac{15}{56} + \frac{15}{56} = \frac{30}{56} = \frac{15}{28}$$

**Check.** The three mutually exclusive, exhaustive outcomes (both red, both blue, different) must have probabilities summing to 1:

$$P(BB) = \frac{3}{8} \times \frac{2}{7} = \frac{6}{56} = \frac{3}{28}$$

$$P(RR) + P(BB) + P(\text{different}) = \frac{20}{56} + \frac{6}{56} + \frac{30}{56} = \frac{56}{56} = 1 \checkmark$$

**Common mistake:** using the same denominator (8) for both draws, as if the ball were replaced — this is the single most common error in "without replacement" questions. For part (b), another common mistake is calculating only one order (e.g. Red-then-Blue) and forgetting to add the Blue-then-Red case, which halves the correct answer.

## Answer

(a) \(P(\text{both red}) = \dfrac{5}{14}\)

(b) \(P(\text{different colours}) = \dfrac{15}{28}\)
