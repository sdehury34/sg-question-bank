---
title: Maximum volume of an open-top box from a fixed area of sheet metal
subject: amath
topic: Applications of Differentiation
level: O-Level
difficulty: Medium
description: Use differentiation to find the dimensions of an open-top square-based box, cut from 108 cm² of sheet metal, that maximise its volume.
date: 2026-07-23
---

## Question

An open-top box with a square base of side \(x\) cm and height \(h\) cm is to be made from \(108\text{ cm}^2\) of sheet metal, with no wastage.

(a) Show that the volume of the box is given by \(\displaystyle V = 27x - \frac{x^3}{4}\).

(b) Find the value of \(x\) for which \(V\) is a maximum, and find this maximum volume.

## Solution

**Step 1 — Set up the surface area constraint.**

The box has a square base and four rectangular sides but no top, so

$$x^2 + 4xh = 108$$

Making \(h\) the subject:

$$h = \frac{108 - x^2}{4x}$$

**Step 2 — Write volume in terms of \(x\) only.**

$$V = x^2 h = x^2 \cdot \frac{108 - x^2}{4x} = \frac{x(108 - x^2)}{4} = \frac{108x - x^3}{4} = 27x - \frac{x^3}{4}$$

This confirms part (a).

**Step 3 — Differentiate and find stationary points.**

$$\frac{dV}{dx} = 27 - \frac{3x^2}{4}$$

Setting \(\dfrac{dV}{dx} = 0\):

$$27 - \frac{3x^2}{4} = 0 \implies x^2 = 36 \implies x = 6 \quad (x > 0)$$

**Step 4 — Confirm it is a maximum.**

$$\frac{d^2V}{dx^2} = -\frac{3x}{2}$$

At \(x = 6\): \(\dfrac{d^2V}{dx^2} = -9 < 0\), so \(V\) is a maximum at \(x = 6\).

**Step 5 — Find the maximum volume.**

$$V = 27(6) - \frac{6^3}{4} = 162 - 54 = 108$$

**Check:** at \(x = 6\), \(h = \dfrac{108 - 36}{4(6)} = \dfrac{72}{24} = 3\), so \(V = x^2h = 36 \times 3 = 108\text{ cm}^3\) — this agrees with the calculus result.

**Common mistake:** using the surface area formula for a closed box (\(2x^2 + 4xh\)) instead of an open-top box (\(x^2 + 4xh\)), which gives the wrong constraint and wrong maximum volume. Also, forgetting the second-derivative (or sign) test means a stationary point is asserted to be a maximum without justification.

## Answer

\(x = 6\text{ cm}\), giving a maximum volume of \(V = 108\text{ cm}^3\) (with height \(h = 3\text{ cm}\)).
