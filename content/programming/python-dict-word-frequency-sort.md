---
title: Predicting the output of a Python word-frequency counter sorted by count
subject: programming
topic: Dictionaries
level: Poly / University
difficulty: Medium
description: Trace a Python dictionary-based word frequency counter and predict its exact printed output after sorting by count then name.
date: 2026-07-10
---

## Question

What is the exact output of the following Python program?

```python
counts = {}
words = ["bird", "cat", "dog", "cat", "dog", "cat"]
for w in words:
    counts[w] = counts.get(w, 0) + 1

pairs = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
for word, freq in pairs:
    print(f"{word}: {freq}")
```

## Solution

**Step 1 — build the frequency dictionary.**

The loop walks through `words` in order, using `dict.get(w, 0)` to read the current count (0 if `w` is not yet a key) and adding 1:

| word processed | `counts` after this step |
|---|---|
| "bird" | `{"bird": 1}` |
| "cat" | `{"bird": 1, "cat": 1}` |
| "dog" | `{"bird": 1, "cat": 1, "dog": 1}` |
| "cat" | `{"bird": 1, "cat": 2, "dog": 1}` |
| "dog" | `{"bird": 1, "cat": 2, "dog": 2}` |
| "cat" | `{"bird": 1, "cat": 3, "dog": 2}` |

So `counts = {"bird": 1, "cat": 3, "dog": 2}`, with keys in **insertion order**: bird, cat, dog (Python dicts preserve insertion order, but that is not the order printed — see step 2).

**Step 2 — sort by the given key.**

`sorted(counts.items(), key=lambda x: (-x[1], x[0]))` sorts the `(word, freq)` pairs by *descending* frequency first (`-x[1]`), then alphabetically by word (`x[0]`) to break ties. The frequencies are bird=1, cat=3, dog=2, all distinct, so the tie-break never triggers here — the pairs are simply ordered from highest to lowest frequency:

$$(\text{"cat"}, 3),\ (\text{"dog"}, 2),\ (\text{"bird"}, 1)$$

**Step 3 — print.**

Each pair is printed as `f"{word}: {freq}"`.

**Verification:** running this exact program prints:
```
cat: 3
dog: 2
bird: 1
```
which matches the traced order above.

**Common mistake:** Assuming the printed order follows the dictionary's insertion order (bird, cat, dog) because Python 3.7+ dicts remember insertion order. That fact is true but irrelevant here — the explicit `sorted(...)` call overrides it and reorders the pairs by frequency.

## Answer

```
cat: 3
dog: 2
bird: 1
```
