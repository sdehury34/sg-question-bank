---
title: Building a binary search tree by insertion and finding its in-order traversal and height
subject: data-structures
topic: Binary Search Trees
level: Poly / University
difficulty: Medium
description: Insert a sequence of keys into an empty binary search tree, then determine its structure, in-order traversal and height.
date: 2026-07-10
---

## Question

Starting from an empty binary search tree (BST), the following keys are inserted **in this order**:

```
50, 30, 70, 20, 40, 60, 80, 10
```

Each key is inserted using the standard BST rule: at each node, go left if the new key is smaller, go right otherwise, until an empty spot is found.

(a) State the parent and children of every node in the resulting tree.

(b) State the sequence of keys produced by an in-order traversal.

(c) State the height of the tree, using the convention that a tree with a single node (the root only) has height 0.

## Solution

**(a) Building the tree**

Insert one key at a time, always starting the comparison at the root:

- **50** → tree is empty, becomes the root.
- **30** → \(30 < 50\), goes left of 50.
- **70** → \(70 > 50\), goes right of 50.
- **20** → \(20 < 50\), left to 30; \(20 < 30\), left of 30.
- **40** → \(40 < 50\), left to 30; \(40 > 30\), right of 30.
- **60** → \(60 > 50\), right to 70; \(60 < 70\), left of 70.
- **80** → \(80 > 50\), right to 70; \(80 > 70\), right of 70.
- **10** → \(10 < 50\), left to 30; \(10 < 30\), left to 20; \(10 < 20\), left of 20.

The resulting tree:

```
              50
            /    \
          30       70
         /  \      /  \
       20    40  60    80
      /
    10
```

Parent/children table:

| Node | Parent | Left child | Right child |
|---|---|---|---|
| 50 | — (root) | 30 | 70 |
| 30 | 50 | 20 | 40 |
| 70 | 50 | 60 | 80 |
| 20 | 30 | 10 | — |
| 40 | 30 | — | — |
| 60 | 70 | — | — |
| 80 | 70 | — | — |
| 10 | 20 | — | — |

**(b) In-order traversal**

In-order traversal visits left subtree, then the node, then right subtree, recursively. For a BST this always produces the keys in ascending sorted order:
$$10, 20, 30, 40, 50, 60, 70, 80$$

**Check:** the original input contains exactly these 8 keys, and the in-order result is simply them sorted — consistent with the BST property that every left descendant is smaller and every right descendant is larger than its ancestor.

**(c) Height of the tree**

The height is the number of edges on the longest path from the root to a leaf. The longest path is \(50 \to 30 \to 20 \to 10\), which has 3 edges. Every other leaf (40, 60, 80) is only 2 edges from the root, so the longest path determines the height:
$$\text{height} = 3$$

**Common mistake:** Confusing *height* (measured in edges, longest root-to-leaf path) with the *number of levels* (measured in nodes). Counting levels instead of edges gives 4 instead of the correct height of 3 — always check which convention the question specifies.

## Answer

In-order traversal: 10, 20, 30, 40, 50, 60, 70, 80. Height of the tree: 3.
