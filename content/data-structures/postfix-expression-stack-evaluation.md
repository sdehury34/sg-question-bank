---
title: Evaluating a postfix expression using a stack
subject: data-structures
topic: Stacks and Queues
level: Poly / University
difficulty: Medium
description: Step through a stack-based algorithm to evaluate the postfix expression 6 2 3 + - 3 8 2 / * + and find its final value.
date: 2026-07-07
---

## Question

Evaluate the following postfix (Reverse Polish Notation) expression using a stack-based algorithm:

```
6 2 3 + - 3 8 2 / * +
```

Show the contents of the stack after each token is processed, and state the final result.

## Solution

**Algorithm.** Scan the tokens left to right:

- If the token is a number, push it onto the stack.
- If the token is an operator, pop the top two values — call the first pop `b` (the top of the stack) and the second pop `a` — compute `a op b`, and push the result back.

Popping in the order "second-popped `op` first-popped" (i.e. `a op b`) is essential for the non-commutative operators `-` and `/`, since the operand pushed **earlier** is the left-hand side of the operation.

**Trace:**

| Token | Action | Stack after |
|---|---|---|
| 6 | push 6 | [6] |
| 2 | push 2 | [6, 2] |
| 3 | push 3 | [6, 2, 3] |
| + | pop 3, 2 → 2 + 3 = 5, push 5 | [6, 5] |
| - | pop 5, 6 → 6 − 5 = 1, push 1 | [1] |
| 3 | push 3 | [1, 3] |
| 8 | push 8 | [1, 3, 8] |
| 2 | push 2 | [1, 3, 8, 2] |
| / | pop 2, 8 → 8 ÷ 2 = 4, push 4 | [1, 3, 4] |
| * | pop 4, 3 → 3 × 4 = 12, push 12 | [1, 12] |
| + | pop 12, 1 → 1 + 12 = 13, push 13 | [13] |

**Check by converting to infix.** The expression corresponds to \( 6 - (2+3) + 3 \times (8 \div 2) \):

$$6 - (2+3) + 3 \times (8 \div 2) = 6 - 5 + 3 \times 4 = 1 + 12 = 13$$

This matches the stack trace, confirming the result.

**Common mistake:** for the non-commutative operators `-` and `/`, popping the two operands and computing them in the wrong order — i.e. `(first-popped) − (second-popped)` instead of `(second-popped) − (first-popped)`. For the `-` step above this would wrongly give \(5 - 6 = -1\) instead of the correct \(6 - 5 = 1\), and every later step built on it would also be wrong.

## Answer

The stack holds a single value, **13**, at the end of evaluation.
