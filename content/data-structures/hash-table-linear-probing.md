---
title: Resolving collisions with linear probing in a hash table
subject: data-structures
topic: Hashing
level: Poly / University
difficulty: Medium
description: Walk through inserting five keys into a size-7 hash table with linear probing, showing every collision and the resulting final table layout.
date: 2026-07-12
---

## Question

A hash table has 7 slots, indexed 0 to 6, and uses the hash function \( h(k) = k \bmod 7 \). Collisions are resolved by **linear probing** (on a collision, try the next index, wrapping around to 0 after index 6, until an empty slot is found).

Insert the keys **23, 44, 21, 30, 15**, in that order. For each key, state its home index \( h(k) \), the index it is finally stored at, and give the final contents of the table.

## Solution

Compute \( h(k) = k \bmod 7 \) for each key first, then insert in order, probing forward on collision.

| Key | \( h(k) \) | Slot(s) checked | Stored at |
|---|---|---|---|
| 23 | \( 23 \bmod 7 = 2 \) | 2 (empty) | **2** |
| 44 | \( 44 \bmod 7 = 2 \) | 2 (taken by 23) → 3 (empty) | **3** |
| 21 | \( 21 \bmod 7 = 0 \) | 0 (empty) | **0** |
| 30 | \( 30 \bmod 7 = 2 \) | 2 (taken) → 3 (taken) → 4 (empty) | **4** |
| 15 | \( 15 \bmod 7 = 1 \) | 1 (empty) | **1** |

So key 44 needed 1 extra probe (collided with 23), and key 30 needed 2 extra probes (collided with 23, then 44).

**Verification (simulated in Python):**

```python
size = 7
keys = [23, 44, 21, 30, 15]
table = [None] * size
for k in keys:
    idx = k % size
    while table[idx] is not None:
        idx = (idx + 1) % size
    table[idx] = k
print(table)
```

Output: `[21, 15, 23, 44, 30, None, None]`, which matches the table built by hand.

**Common mistake:** Re-hashing the key with a different formula after a collision (e.g., trying \( (k+1) \bmod 7 \)) instead of keeping the *original* key's hash and simply scanning forward index-by-index from that position — linear probing always probes table *positions*, not re-hashed key values.

## Answer

Final table (index: value): `0: 21, 1: 15, 2: 23, 3: 44, 4: 30, 5: —, 6: —`
