---
title: Preorder, inorder and postorder traversal of a binary tree
subject: data-structures
topic: Binary Trees
level: Poly / University
difficulty: Medium
description: Derive the preorder, inorder and postorder traversal sequences of a given binary tree and verify them against a recursive implementation.
date: 2026-07-11
---

## Question

Consider the following binary tree:

```
        F
      /   \
     B     G
    / \     \
   A   D     I
      / \   /
     C   E H
```

List the sequence of nodes visited in:

(a) **Preorder** traversal (root, left, right)
(b) **Inorder** traversal (left, root, right)
(c) **Postorder** traversal (left, right, root)

## Solution

Work outward from the leaves. Node `D` has children `C` (left) and `E` (right). Node `B` has children `A` (left) and `D` (right, the subtree just described). Node `I` has child `H` (left) and no right child. Node `G` has no left child and child `I` (right, the subtree just described). The root `F` has children `B` (left) and `G` (right).

**(a) Preorder (root → left → right).**

Visit `F`, then recurse into the left subtree rooted at `B`, then the right subtree rooted at `G`.

- `F` → `B` → `A` → `D` → `C` → `E` → `G` → `I` → `H`

**(b) Inorder (left → root → right).**

Fully visit the left subtree, then the root, then the right subtree.

- Left subtree of `F` (rooted at `B`): `A`, `B`, `C`, `D`, `E`
- Root: `F`
- Right subtree of `F` (rooted at `G`): `G`, `H`, `I`

Combined: `A` → `B` → `C` → `D` → `E` → `F` → `G` → `H` → `I`

**(c) Postorder (left → right → root).**

Fully visit the left subtree, then the right subtree, then the root.

- Left subtree of `F`: `A`, `C`, `E`, `D`, `B`
- Right subtree of `F`: `H`, `I`, `G`
- Root: `F`

Combined: `A` → `C` → `E` → `D` → `B` → `H` → `I` → `G` → `F`

**Check.** All three sequences contain each of the 9 nodes exactly once, and in the inorder sequence every node's left-subtree nodes appear before it and right-subtree nodes appear after it (e.g. `D`'s children `C`, `E` sit immediately either side of `D`), which is the defining property of an inorder traversal. This was also verified by running a standard recursive traversal against this exact tree structure in Python, which reproduced the same three sequences.

**Common mistake:** confusing inorder and postorder for the root's position, or forgetting that a node with only a right child (like `I`, whose only child `H` is on the *left*) still visits its single child before or after itself according to the traversal's left/right rule — `H` is `I`'s left child, so preorder visits `I` before `H`, but inorder and postorder both visit `H` before `I`.

## Answer

Preorder: F, B, A, D, C, E, G, I, H
Inorder: A, B, C, D, E, F, G, H, I
Postorder: A, C, E, D, B, H, I, G, F
