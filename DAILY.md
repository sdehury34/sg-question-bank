# ☀️ Daily Playbook — SG Question Bank

Open this file every morning. The whole job is ~15 minutes.

---

## The 15-minute routine

### 1. Open today's pull request (1 min)

→ **https://github.com/sdehury34/sg-question-bank/pulls**

There should be a PR titled `Daily questions — <today's date>`, opened around
7:00–7:15 AM by the scheduled Claude routine. It contains 5 new questions.

### 2. Review the 5 questions (~10 min, ~2 min each)

Open the **Files changed** tab. For each question, check:

- [ ] **Is the final answer correct?** Skim the solution; punch the key
      calculation into a calculator if it's math, or eyeball the code logic.
      This is the single most important check — your site's reputation is
      "the solutions are actually right."
- [ ] **Does the question make sense?** No missing information, no ambiguity,
      difficulty label is honest.
- [ ] **Is it a duplicate?** If it feels like a near-copy of an existing
      question, it probably is — reject that file.
- [ ] **Syllabus-appropriate?** Right level (O-Level / A-Level / poly),
      3 s.f. answers, correct units.

You do NOT need to check formatting, file naming, or whether the site builds —
the routine already validated the build before opening the PR.

### 3. Act on it (1 min)

| Situation | What to do |
|---|---|
| All 5 look good | Click **Merge pull request** → **Confirm**. Done — the site auto-deploys in ~2 min. |
| One question has a small error | Edit the file directly in the PR (pencil icon on the file in Files changed), commit to the same branch, then merge. |
| One question is bad beyond fixing | In Files changed, delete that file from the branch (… menu → Delete file), then merge the remaining 4. |
| The whole batch is bad | Close the PR without merging. Tomorrow's run starts fresh. |

### 4. Quick glance at the site (1 min, optional)

→ **https://sdehury34.github.io/sg-question-bank/**

Confirm the new questions appear under "Latest questions" a few minutes after
merging.

---

## Weekly (~5 min, e.g. every Sunday)

- [ ] **Traffic:** https://sg-question-bank.goatcounter.com — any visitors?
      Which pages? (Rising pages = topics worth generating more of.)
- [ ] **Google indexing:** https://search.google.com/search-console →
      *Pages* report — how many pages are indexed? This number should climb
      week over week. Also confirm the sitemap status says **Success**.
- [ ] **Merged everything?** Check there are no forgotten open PRs piling up.

---

## Milestones — message Claude when these happen

| Trigger | What we do next |
|---|---|
| GoatCounter shows steady daily visitors | Build the **weekly analytics routine** — it writes `data/analytics-summary.md` so daily generation automatically favors high-traffic topics (the self-learning loop). |
| ~50 visitors/day | Add a **Stripe Payment Link** to `support_link` in `config.json` and start monetizing. |
| A subject clearly dominates traffic | Consider a new dedicated subject or topic cluster. |

---

## Troubleshooting

**No PR this morning?**
Check the routine's run history: https://claude.ai/code/routines/trig_01AAWPEMhcMjMuAfAUqBPgXu
It may have failed or pushed a branch without opening a PR — look for a
`daily/<date>` branch at https://github.com/sdehury34/sg-question-bank/branches
and open the PR manually from there. One missed day costs nothing.

**Site didn't update after merging?**
Check the deploy run: https://github.com/sdehury34/sg-question-bank/actions
A red ❌ means the build failed — open the log, or paste it to Claude.

**Want to change the schedule, model, or instructions?**
The routine's prompt lives at the routines page above; the content rules live
in `ROUTINE.md` in this folder (edit + push, the routine reads it fresh every
run).

**Want to add a question yourself?**
Drop a markdown file in `content/<subject>/` following the format in
`ROUTINE.md`, then:

```
python scripts/build.py     # must pass
git add -A && git commit -m "Add question" && git push
```

---

## All links in one place

| What | URL |
|---|---|
| Today's PR | https://github.com/sdehury34/sg-question-bank/pulls |
| Live site | https://sdehury34.github.io/sg-question-bank/ |
| Traffic | https://sg-question-bank.goatcounter.com |
| Google Search Console | https://search.google.com/search-console |
| Deploy status | https://github.com/sdehury34/sg-question-bank/actions |
| Daily routine (schedule/history) | https://claude.ai/code/routines/trig_01AAWPEMhcMjMuAfAUqBPgXu |
| Content rules | `ROUTINE.md` in this folder |
