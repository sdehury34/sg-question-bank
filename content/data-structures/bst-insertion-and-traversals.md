---
title: Building a binary search tree and finding its traversals
subject: data-structures
topic: Binary Search Trees
level: Poly / University
difficulty: Medium
description: Insert a sequence of keys into an empty binary search tree and derive its in-order, pre-order, and post-order traversals plus its height.
date: 2026-07-19
---

## Question

Starting from an empty binary search tree (BST), insert the following keys **in this order**:

```
50, 30, 70, 20, 40, 60, 80, 10, 25
```

(a) Describe the resulting tree (give each node's left and right child).

(b) Write out the in-order, pre-order, and post-order traversals of the tree.

(c) State the height of the tree (the number of edges on the longest root-to-leaf path).

## Solution

**Step 1 — Insert the keys one at a time.**

Each key is compared against the current node starting from the root: go left if smaller, right if greater-or-equal, until an empty spot is found.

- Insert 50 → becomes the root.
- Insert 30 → 30 < 50, goes left of 50.
- Insert 70 → 70 ≥ 50, goes right of 50.
- Insert 20 → 20 < 50, < 30, goes left of 30.
- Insert 40 → 40 < 50, ≥ 30, goes right of 30.
- Insert 60 → 60 ≥ 50, < 70, goes left of 70.
- Insert 80 → 80 ≥ 50, ≥ 70, goes right of 70.
- Insert 10 → 10 < 50, < 30, < 20, goes left of 20.
- Insert 25 → 25 < 50, < 30, ≥ 20, goes right of 20.

**Resulting structure:**

```
                50
              /    \
            30      70
           /  \     /  \
         20    40  60   80
        /  \
      10    25
```

| Node | Left child | Right child |
|---|---|---|
| 50 | 30 | 70 |
| 30 | 20 | 40 |
| 70 | 60 | 80 |
| 20 | 10 | 25 |
| 40 | — | — |
| 60 | — | — |
| 80 | — | — |
| 10 | — | — |
| 25 | — | — |

**Step 2 — Traversals.**

- **In-order** (left, node, right) visits keys in ascending order for a BST:
  $$10, 20, 25, 30, 40, 50, 60, 70, 80$$
- **Pre-order** (node, left, right):
  $$50, 30, 20, 10, 25, 40, 70, 60, 80$$
- **Post-order** (left, right, node):
  $$10, 25, 20, 40, 30, 60, 80, 70, 50$$

**Step 3 — Height.**

The longest root-to-leaf path is \(50 \to 30 \to 20 \to 10\) (or \(50 \to 30 \to 20 \to 25\)), which has 3 edges. So the height of the tree is **3**.

**Check.** The in-order traversal, \(10, 20, 25, 30, 40, 50, 60, 70, 80\), is fully sorted in ascending order — this is a required property of every valid BST's in-order traversal, confirming the tree was built correctly. Running the insertion and traversal algorithm in code reproduces exactly these three sequences and a height of 3.

**Common mistake:** confusing pre-order and post-order, or forgetting that "height" counts **edges** on the longest path, not the number of nodes (which would give 4 here, not 3) — different textbooks define height either way, so always state which convention is being used.

## Answer

(a) See the tree diagram and left/right-child table above.

(b) In-order: 10, 20, 25, 30, 40, 50, 60, 70, 80. Pre-order: 50, 30, 20, 10, 25, 40, 70, 60, 80. Post-order: 10, 25, 20, 40, 30, 60, 80, 70, 50.

(c) The height of the tree is **3**.
