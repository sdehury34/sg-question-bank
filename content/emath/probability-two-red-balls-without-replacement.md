---
title: Probability of drawing two red balls without replacement from a bag
subject: emath
topic: Probability
level: O-Level
difficulty: Medium
description: Find the probability of drawing two red balls in a row, without replacement, from a bag of 5 red and 3 blue balls.
date: 2026-07-09
---

## Question

A bag contains 5 red balls and 3 blue balls. Two balls are drawn at random from the bag, one after another, **without replacement**. Find the probability that both balls drawn are red.

## Solution

**Step 1 — Probability the first ball is red.** There are 8 balls in total, 5 of which are red:

$$P(\text{1st red}) = \frac{5}{8}$$

**Step 2 — Probability the second ball is red, given the first was red.** After removing one red ball, 7 balls remain, of which 4 are red:

$$P(\text{2nd red} \mid \text{1st red}) = \frac{4}{7}$$

**Step 3 — Multiply along the branch** (since the events are dependent):

$$P(\text{both red}) = \frac{5}{8} \times \frac{4}{7} = \frac{20}{56} = \frac{5}{14}$$

**Check (using combinations):** the number of ways to choose 2 red balls from 5 is \(\binom{5}{2} = 10\); the number of ways to choose any 2 balls from 8 is \(\binom{8}{2} = 28\). So

$$P(\text{both red}) = \frac{\binom{5}{2}}{\binom{8}{2}} = \frac{10}{28} = \frac{5}{14} \checkmark$$

This agrees with the tree-diagram method, confirming the answer.

**Common mistake:** treating the draws as independent and calculating \(\frac{5}{8} \times \frac{5}{8}\) (as if the first ball were replaced). Because the ball is *not* replaced, both the number of red balls and the total number of balls decrease by 1 for the second draw.

## Answer

$$P(\text{both red}) = \frac{5}{14}$$
