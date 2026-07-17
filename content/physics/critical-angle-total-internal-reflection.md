---
title: Finding the critical angle for glass and checking for total internal reflection
subject: physics
topic: Refraction of Light
level: O-Level
difficulty: Medium
description: Calculate the critical angle for a glass-air boundary given the refractive index, then determine whether a 45° ray undergoes total internal reflection.
date: 2026-07-18
---

## Question

A block of glass has refractive index \(n = 1.52\) for light travelling from glass into air.

(a) Calculate the critical angle \(C\) for the glass-air boundary, to 1 decimal place.

(b) A ray of light inside the glass strikes the glass-air boundary at an angle of incidence of \(45^\circ\), measured from the normal. State, with a reason, whether the ray undergoes total internal reflection.

## Solution

**Part (a) — critical angle.** The critical angle is the angle of incidence (in the denser medium) for which the angle of refraction is exactly \(90^\circ\). Applying Snell's law at the glass-air boundary,

$$n \sin C = 1 \times \sin 90^\circ$$

$$\sin C = \frac{1}{n} = \frac{1}{1.52} = 0.6579\ (\text{4 s.f.})$$

$$C = \sin^{-1}(0.6579) = 41.1^\circ\ (\text{1 d.p.})$$

**Check:** substituting back, \(\sin(41.1^\circ) = 0.658\), and \(1/1.52 = 0.658\) — consistent (verified numerically).

**Part (b) — is there total internal reflection?** Total internal reflection occurs when light travels from a denser to a less dense medium **and** the angle of incidence exceeds the critical angle. Here the ray travels from glass (denser) to air (less dense), and

$$45^\circ > C = 41.1^\circ$$

so both conditions are satisfied.

**Common mistake:** using \(\sin C = n\) instead of \(\sin C = 1/n\) (mixing up which medium is denser), or concluding TIR occurs whenever the angle is "large" without actually comparing it to the calculated critical angle — a ray at, say, \(35^\circ\) would simply refract and partially reflect, since \(35^\circ < 41.1^\circ\).

## Answer

(a) Critical angle \(C = 41.1^\circ\)

(b) Yes — since the ray travels from the denser medium (glass) to the less dense medium (air) and its angle of incidence \(45^\circ\) is greater than the critical angle \(41.1^\circ\), total internal reflection occurs.
