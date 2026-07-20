---
title: Calculating water pressure and force at the bottom of a tank
subject: physics
topic: Pressure
level: O-Level
difficulty: Medium
description: Find the pressure due to water and the total pressure at the bottom of a 2.5 m deep tank, then the force on a small hole, using p = hρg.
date: 2026-07-21
---

## Question

A tank contains water to a depth of 2.5 m. The density of water is \(1000\ \text{kg/m}^3\), atmospheric pressure is \(1.0 \times 10^5\ \text{Pa}\), and \(g = 10\ \text{N/kg}\).

1. Calculate the pressure due to the water alone at the bottom of the tank.
2. Calculate the total pressure (water + atmosphere) at the bottom of the tank.
3. A small hole of cross-sectional area \(2\ \text{cm}^2\) is opened at the bottom. Calculate the force exerted by the water alone on this hole.

## Solution

**Part 1.** Pressure due to a liquid column is given by \(p = h\rho g\), where \(h\) is the depth, \(\rho\) is the density, and \(g\) is the gravitational field strength:

$$p_{\text{water}} = h\rho g = (2.5)(1000)(10) = 25\,000\ \text{Pa} = 2.5 \times 10^4\ \text{Pa}$$

**Part 2.** The total pressure at the bottom is the pressure due to the water plus the atmospheric pressure pushing down on the surface:

$$p_{\text{total}} = p_{\text{atm}} + p_{\text{water}} = 1.0 \times 10^5 + 2.5 \times 10^4 = 1.25 \times 10^5\ \text{Pa}$$

**Part 3.** Force is pressure times area, \(F = pA\). Only the water pressure is asked for here, so use \(p_{\text{water}}\), and convert the area to \(\text{m}^2\) first:

$$A = 2\ \text{cm}^2 = 2 \times 10^{-4}\ \text{m}^2$$

$$F = p_{\text{water}} \times A = (25\,000)(2 \times 10^{-4}) = 5.0\ \text{N}$$

**Check.** Working part 3 in cm-based units as a sanity check: \(25\,000\ \text{Pa} = 2.5\ \text{N/cm}^2\), so \(F = 2.5 \times 2 = 5.0\ \text{N}\ \checkmark\), matching the SI calculation.

**Common mistake:** forgetting to convert the hole's area from cm² to m² before multiplying by pressure in Pa (which is N/m²). Using \(A = 2\) (cm²) directly gives a force 10,000 times too large.

## Answer

1. Pressure due to water alone = **\(2.5 \times 10^4\) Pa**
2. Total pressure at the bottom = **\(1.25 \times 10^5\) Pa**
3. Force on the hole due to water = **5.0 N**
