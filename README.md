# SG Question Bank

Free practice questions with full worked solutions for Singapore students —
O-Level, A-Level, poly and university modules. New questions are generated
daily by a scheduled Claude routine, reviewed by a human, and deployed
automatically to GitHub Pages.

## How it works

```
scheduled Claude routine (daily)
        │  writes 5 new questions, opens a PR
        ▼
you review & merge (~15 min)
        │  push to main
        ▼
GitHub Actions builds the site (scripts/build.py)
        │
        ▼
GitHub Pages serves it → students find pages via Google search
```

## Local development

```
python scripts/build.py     # builds the site into dist/
```

No dependencies beyond Python 3.10+. Open `dist/index.html` in a browser to
preview (or `python -m http.server -d dist` for correct absolute links).

## Adding content

See `ROUTINE.md` for the content format and quality rules. Drop a markdown
file into `content/<subject>/` and rebuild.

## Configuration (`config.json`)

- `base_url` — set to your GitHub Pages URL (e.g.
  `https://<username>.github.io/sg-question-bank`) to enable sitemap.xml and
  canonical tags.
- `analytics_snippet` — paste a Cloudflare Web Analytics or GoatCounter
  `<script>` tag here to enable free analytics.
- `support_link` — a Stripe Payment Link (or Buy Me a Coffee URL); when set,
  a support call-to-action appears under each solution.
