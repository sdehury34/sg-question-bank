---
title: Predicting the output of a Python word-count dictionary program
subject: programming
topic: Dictionaries
level: Poly / University
difficulty: Medium
description: Predict the printed output of Python code that counts word frequencies with a dictionary and sorts the results by count then alphabetically.
date: 2026-07-22
---

## Question

What does the following Python code print?

```python
d = {}
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
for w in words:
    d[w] = d.get(w, 0) + 1

print(sorted(d.items(), key=lambda x: (-x[1], x[0])))
```

## Solution

**Step 1 — Build the frequency dictionary.** The loop walks through `words` and, for each word `w`, does `d[w] = d.get(w, 0) + 1`. `dict.get(w, 0)` returns the current count for `w`, or `0` if `w` is not yet a key, so this pattern increments a running count without a `KeyError` on the first occurrence.

Tracing it word by word:

| word | `d.get(w, 0)` | new `d[w]` | `d` after |
|---|---|---|---|
| apple | 0 | 1 | `{'apple': 1}` |
| banana | 0 | 1 | `{'apple': 1, 'banana': 1}` |
| apple | 1 | 2 | `{'apple': 2, 'banana': 1}` |
| cherry | 0 | 1 | `{'apple': 2, 'banana': 1, 'cherry': 1}` |
| banana | 1 | 2 | `{'apple': 2, 'banana': 2, 'cherry': 1}` |
| apple | 2 | 3 | `{'apple': 3, 'banana': 2, 'cherry': 1}` |

Final counts: `apple: 3, banana: 2, cherry: 1`.

**Step 2 — Sort with the key function.** `sorted(d.items(), key=lambda x: (-x[1], x[0]))` sorts the `(word, count)` pairs by a tuple: first by `-count` ascending (i.e. count descending), and ties broken by `x[0]` (the word) ascending alphabetically. Since all three counts here are distinct, the tie-break never comes into play — the pairs sort purely by count descending:

$$\text{apple}(3) \to \text{banana}(2) \to \text{cherry}(1)$$

**Verification (Python, actually run):**

```python
d = {}
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
for w in words:
    d[w] = d.get(w, 0) + 1

print(sorted(d.items(), key=lambda x: (-x[1], x[0])))
```

Running this prints:

```
[('apple', 3), ('banana', 2), ('cherry', 1)]
```

which matches the hand trace.

**Common mistake:** writing the counting loop as `d[w] += 1` instead of `d[w] = d.get(w, 0) + 1`. `+=` requires the key to already exist, so this raises a `KeyError` the first time a new word is seen (e.g. on `"apple"` the very first iteration) — `.get(w, 0)` is what safely supplies the starting count of `0` for words not yet in the dictionary.

## Answer

```
[('apple', 3), ('banana', 2), ('cherry', 1)]
```
