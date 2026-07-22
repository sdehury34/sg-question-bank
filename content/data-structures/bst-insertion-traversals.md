---
title: Binary search tree insertion order and traversal sequences
subject: data-structures
topic: Binary Search Trees
level: Poly / University
difficulty: Medium
description: Insert a sequence of keys into an empty binary search tree and derive its in-order, pre-order and post-order traversals plus its height.
date: 2026-07-23
---

## Question

The keys \(50, 30, 70, 20, 40, 60, 80, 10\) are inserted, in that order, into an initially empty binary search tree (BST). Each key is inserted by starting at the root and moving left if the key is smaller than the current node, or right if it is larger or equal, until an empty position is found.

(a) Draw the resulting BST.

(b) State the in-order, pre-order and post-order traversal sequences of the tree.

(c) State the height of the tree, where the height of a single-node tree is 0.

## Solution

**Step 1 — Insert the keys one at a time.**

- Insert 50 → becomes the root.
- Insert 30 → \(30 < 50\), goes left of 50.
- Insert 70 → \(70 > 50\), goes right of 50.
- Insert 20 → \(20 < 50\), then \(20 < 30\), goes left of 30.
- Insert 40 → \(40 < 50\), then \(40 > 30\), goes right of 30.
- Insert 60 → \(60 > 50\), then \(60 < 70\), goes left of 70.
- Insert 80 → \(80 > 50\), then \(80 > 70\), goes right of 70.
- Insert 10 → \(10 < 50\), then \(10 < 30\), then \(10 < 20\), goes left of 20.

**Step 2 — The resulting tree.**

```
            50
          /    \
        30      70
       /  \    /  \
      20  40  60   80
     /
    10
```

**Step 3 — Traverse the tree.**

**In-order** (left, node, right) visits nodes in ascending sorted order for any BST — a useful self-check:

$$10,\ 20,\ 30,\ 40,\ 50,\ 60,\ 70,\ 80$$

**Pre-order** (node, left, right):

$$50,\ 30,\ 20,\ 10,\ 40,\ 70,\ 60,\ 80$$

**Post-order** (left, right, node):

$$10,\ 20,\ 40,\ 30,\ 60,\ 80,\ 70,\ 50$$

**Step 4 — Height of the tree.**

The longest root-to-leaf path is \(50 \to 30 \to 20 \to 10\), which has 3 edges. With the height of a single node defined as 0, the height of the tree is **3**.

**Verification (run in Python):**

```python
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def inorder(root, out):
    if root:
        inorder(root.left, out); out.append(root.key); inorder(root.right, out)

def preorder(root, out):
    if root:
        out.append(root.key); preorder(root.left, out); preorder(root.right, out)

def postorder(root, out):
    if root:
        postorder(root.left, out); postorder(root.right, out); out.append(root.key)

def height(root):
    if root is None:
        return -1
    return 1 + max(height(root.left), height(root.right))

root = None
for k in [50, 30, 70, 20, 40, 60, 80, 10]:
    root = insert(root, k)

io, pre, post = [], [], []
inorder(root, io); preorder(root, pre); postorder(root, post)
print(io)    # [10, 20, 30, 40, 50, 60, 70, 80]
print(pre)   # [50, 30, 20, 10, 40, 70, 60, 80]
print(post)  # [10, 20, 40, 30, 60, 80, 70, 50]
print(height(root))  # 3
```

Running this script prints exactly the sequences and height derived by hand above.

**Common mistake:** confusing pre-order and post-order — pre-order visits the node before its subtrees, post-order after. Another common error is computing height by counting nodes instead of edges on the longest path, which would overstate the height by 1.

## Answer

In-order: \(10, 20, 30, 40, 50, 60, 70, 80\)
Pre-order: \(50, 30, 20, 10, 40, 70, 60, 80\)
Post-order: \(10, 20, 40, 30, 60, 80, 70, 50\)
Height: \(3\)
