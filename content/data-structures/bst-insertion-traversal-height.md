---
title: Building a binary search tree and finding its in-order traversal and height
subject: data-structures
topic: Trees
level: Poly / University
difficulty: Medium
description: Insert a sequence of values into an empty binary search tree, then find the resulting in-order traversal and the tree's height.
date: 2026-07-22
---

## Question

Starting from an empty binary search tree (BST), the following values are inserted in this order:

```
50, 30, 70, 20, 40, 60, 80, 10
```

(a) State the in-order traversal of the resulting tree.

(b) State the height of the tree, counting the number of edges on the longest root-to-leaf path.

## Solution

**Step 1 — Insert each value.** In a BST, each new value is compared against nodes starting from the root: smaller values go left, larger (or equal) values go right, descending until an empty spot is found.

- `50` → becomes the root.
- `30` → \(30 < 50\), goes left of 50.
- `70` → \(70 > 50\), goes right of 50.
- `20` → \(20 < 50\), left; \(20 < 30\), left of 30.
- `40` → \(40 < 50\), left; \(40 > 30\), right of 30.
- `60` → \(60 > 50\), right; \(60 < 70\), left of 70.
- `80` → \(80 > 50\), right; \(80 > 70\), right of 70.
- `10` → \(10 < 50\), left; \(10 < 30\), left; \(10 < 20\), left of 20.

**Step 2 — Resulting tree.**

```
              50
           /      \
         30        70
        /   \      /  \
      20    40    60   80
     /
   10
```

**Step 3 — In-order traversal (part a).** In-order visits left subtree, then node, then right subtree, recursively. For a BST this always yields values in ascending order — a useful check on the build itself:

$$10,\ 20,\ 30,\ 40,\ 50,\ 60,\ 70,\ 80$$

This is sorted, confirming the tree was built correctly (an unsorted in-order output would indicate an insertion error).

**Step 4 — Height (part b).** The longest root-to-leaf path is \(50 \to 30 \to 20 \to 10\), which has 3 edges. Every other leaf (40, 60, 80) is reached in 2 edges or fewer, so the height of the tree is 3.

**Verification (Python, actually run):**

```python
class Node:
    def __init__(self, val):
        self.val, self.left, self.right = val, None, None

def insert(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def inorder(root, out):
    if root:
        inorder(root.left, out)
        out.append(root.val)
        inorder(root.right, out)

def height(root):
    if root is None:
        return -1
    return 1 + max(height(root.left), height(root.right))

root = None
for v in [50, 30, 70, 20, 40, 60, 80, 10]:
    root = insert(root, v)

out = []
inorder(root, out)
print(out)          # [10, 20, 30, 40, 50, 60, 70, 80]
print(height(root)) # 3
```

Running this prints `[10, 20, 30, 40, 50, 60, 70, 80]` and `3`, matching the hand trace.

**Common mistake:** inserting `40` as a left child of `50` because "40 < 50", instead of continuing the comparison down into 30's subtree first — a BST insertion always restarts comparison from the root and only stops descending once an empty slot is reached, so 40 must be compared against 30 (and placed right of it) before it is placed at all.

## Answer

(a) In-order traversal: \(10, 20, 30, 40, 50, 60, 70, 80\)

(b) Height of the tree: **3** (edges on the longest root-to-leaf path)
