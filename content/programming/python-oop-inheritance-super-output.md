---
title: Predicting the output of Python class inheritance with super()
subject: programming
topic: Object-Oriented Programming
level: Poly / University
difficulty: Medium
description: Trace a Python subclass that overrides a method and calls super() to predict the exact printed output, including a stateful battery attribute.
date: 2026-07-16
---

## Question

What is printed when the following program runs?

```python
class Vehicle:
    def __init__(self, make, speed):
        self.make = make
        self.speed = speed

    def describe(self):
        return f"{self.make} at {self.speed} km/h"

    def accelerate(self, amount):
        self.speed += amount
        return self.describe()


class ElectricCar(Vehicle):
    def __init__(self, make, speed, battery):
        super().__init__(make, speed)
        self.battery = battery

    def accelerate(self, amount):
        if self.battery <= 0:
            return f"{self.make} cannot accelerate: battery empty"
        self.battery -= 5
        result = super().accelerate(amount * 2)
        return f"{result}, battery {self.battery}%"


cars = [Vehicle("Toyota", 40), ElectricCar("Tesla", 40, 12)]
for car in cars:
    print(car.accelerate(10))
    print(car.accelerate(10))
```

## Solution

**`Vehicle("Toyota", 40)`** has no overridden `accelerate`, so each call just adds `amount` to `speed` and describes the car:

- 1st call `accelerate(10)`: `speed = 40 + 10 = 50` → prints `Toyota at 50 km/h`
- 2nd call `accelerate(10)`: `speed = 50 + 10 = 60` → prints `Toyota at 60 km/h`

**`ElectricCar("Tesla", 40, 12)`** overrides `accelerate`. Each call first checks `battery <= 0` (false while battery is positive), then deducts 5 from `battery`, then calls `super().accelerate(amount * 2)` — the *parent's* `accelerate`, which adds **double** the requested amount to `speed`:

- 1st call `accelerate(10)`: `battery = 12 - 5 = 7` (not empty, so it proceeds); `super().accelerate(20)` sets `speed = 40 + 20 = 60` and returns `"Tesla at 60 km/h"`; the override appends the battery, printing `Tesla at 60 km/h, battery 7%`
- 2nd call `accelerate(10)`: `battery = 7 - 5 = 2`; `super().accelerate(20)` sets `speed = 60 + 20 = 80`, giving `Tesla at 80 km/h, battery 2%`

**Check.** Running this exact code (verified by execution) prints:
```
Toyota at 50 km/h
Toyota at 60 km/h
Tesla at 60 km/h, battery 7%
Tesla at 80 km/h, battery 2%
```
which matches the trace above line for line.

**Common mistake:** assuming `ElectricCar`'s `speed` increases by the same `amount` passed in (10), forgetting that the override doubles it (`amount * 2`) before delegating to `super().accelerate()` — leading students to (incorrectly) predict `50` and `60` for the Tesla instead of `60` and `80`.

## Answer

```
Toyota at 50 km/h
Toyota at 60 km/h
Tesla at 60 km/h, battery 7%
Tesla at 80 km/h, battery 2%
```
