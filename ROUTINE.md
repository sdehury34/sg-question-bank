# Daily Content Generation Spec

This file is the instruction set for the scheduled Claude routine that generates
new questions every day. It is also useful to a human contributor. Follow it exactly.

## Goal

Add **5 new practice questions** to this repository each day, as a pull request
titled `Daily questions — YYYY-MM-DD`, for the site owner to review and merge.

## Procedure

1. **Read `data/index.json`** to see every existing question (title, subject,
   topic, difficulty). Never duplicate an existing question or a near-variant
   (same method, same numbers).
2. **Read `data/analytics-summary.md` if it exists.** It lists which subjects
   and topics are getting traffic. Weight today's 5 questions toward the
   subjects/topics marked as high-traffic or requested. If the file does not
   exist, rotate fairly: pick the 5 subjects with the fewest questions.
3. **Pick topics that real students search for.** Prefer named syllabus topics
   (e.g. "Integration by Parts", "Mole Concept", "Binary Search") over vague
   ones. Each question's `title` should read like a search query a student
   would type.
4. **Write each question** as `content/<subject>/<slug>.md` following the
   format below. The slug must be lowercase-kebab-case and unique.
5. **Validate:** run `python scripts/build.py`. It must exit successfully with
   no ERROR lines. Fix any problems before committing.
6. **Open a pull request** on a branch named `daily/YYYY-MM-DD` containing the
   5 new content files **and the regenerated `data/index.json`** (the build in
   step 5 updates it — committing it keeps the duplicate-avoidance index
   current). The PR body lists each question title and one line on why that
   topic was chosen.

## Content rules (quality bar)

- Every solution must be **verifiably correct**. Work the problem fully before
  writing it up; check the final answer by substitution or an alternative
  method where possible, and show that check in the solution.
- Follow the Singapore syllabus conventions (O-Level 4048/4049, A-Level 9758,
  and common poly/university module content) — 3 s.f. answers, correct units,
  SI conventions.
- Include one **"Common mistake"** note per math/science question.
- Difficulty must be honest: Easy / Medium / Hard.
- Use MathJax delimiters: `\( ... \)` inline, `$$ ... $$` on its own line for
  display math. Use fenced code blocks for code.
- No copyrighted past-exam questions. Write original questions in the style of
  the syllabus.

## File format

```
---
title: <search-query-style title, no trailing period>
subject: <one of: emath | amath | h2-math | physics | chemistry | programming | data-structures>
topic: <syllabus topic name>
level: <O-Level | A-Level | Poly / University>
difficulty: <Easy | Medium | Hard>
description: <one sentence, ~150 chars, SEO meta description>
date: <YYYY-MM-DD, today>
---

## Question

...

## Solution

...

## Answer

...
```

All three `##` sections are required, in that order. The build fails otherwise.
