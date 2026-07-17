---
title: Tracing output of Python inheritance with super() method overriding
subject: programming
topic: Object-Oriented Programming
level: Poly / University
difficulty: Medium
description: Predict the printed output of a three-level Python class hierarchy that overrides a method and chains calls with super().
date: 2026-07-18
---

## Question

Consider the following Python program:

```python
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def speak(self):
        base = super().speak()
        return f"{base}, specifically a bark"

class Puppy(Dog):
    def speak(self):
        return f"{super().speak()}!!!"

animals = [Animal("Generic"), Dog("Rex"), Puppy("Fido")]
for a in animals:
    print(a.speak())
```

What does this program print?

## Solution

**Walking through each object in the list, in order.**

- `Animal("Generic")` has no overridden `speak`, so calling `.speak()` runs `Animal.speak`, which returns `"Generic makes a sound"`.

- `Dog("Rex")` overrides `speak`. Inside `Dog.speak`, `super().speak()` calls `Animal.speak` on the same object, giving `base = "Rex makes a sound"`. `Dog.speak` then returns `"Rex makes a sound, specifically a bark"`.

- `Puppy("Fido")` overrides `speak` again. Inside `Puppy.speak`, `super().speak()` does **not** jump straight to `Animal` — it follows the Method Resolution Order (MRO) of `Puppy`, which is `Puppy → Dog → Animal → object`. So `super().speak()` here calls `Dog.speak` (the *next* class in the MRO after `Puppy`), which itself calls `super().speak()` to reach `Animal.speak`. That chain produces `"Fido makes a sound, specifically a bark"`, and `Puppy.speak` appends `"!!!"` to get `"Fido makes a sound, specifically a bark!!!"`.

**Verified by running the code (Python 3):**

```
Generic makes a sound
Rex makes a sound, specifically a bark
Fido makes a sound, specifically a bark!!!
```

This matches the trace above exactly.

**Common mistake:** assuming `super()` inside `Puppy.speak` skips directly to `Animal.speak`, bypassing `Dog.speak` (e.g. expecting `"Fido makes a sound!!!"` without the "specifically a bark" part). In reality, `super()` always resolves to the *next class in the MRO*, not to the topmost base class — since `Dog` sits between `Puppy` and `Animal` in the hierarchy, its override still runs as part of the chain.

## Answer

```
Generic makes a sound
Rex makes a sound, specifically a bark
Fido makes a sound, specifically a bark!!!
```
