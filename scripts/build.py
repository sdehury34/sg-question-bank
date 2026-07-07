"""Static site builder for SG Question Bank.

Zero external dependencies. Reads markdown question files from content/,
writes a complete static site to dist/.

Content file format (content/<subject>/<slug>.md):

    ---
    title: Solving a quadratic by completing the square
    subject: emath
    topic: Quadratic Equations
    level: O-Level
    difficulty: Medium
    description: One-line SEO description of the question.
    date: 2026-07-07
    ---

    ## Question
    ...markdown...

    ## Solution
    ...markdown...

    ## Answer
    ...markdown...

Math: use MathJax delimiters \\( \\) inline and $$ $$ for display math.
The markdown converter is deliberately conservative so math is never mangled:
it supports headings, fenced code blocks, `inline code`, **bold**, lists,
and paragraphs. It does NOT process underscores or single asterisks.
"""

import html
import json
import re
import shutil
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
DIST = ROOT / "dist"
CONFIG = json.loads((ROOT / "config.json").read_text(encoding="utf-8"))

# Internal links are prefixed with the path component of base_url so the site
# works when served from a subpath (e.g. https://user.github.io/sg-question-bank/).
PREFIX = urlparse(CONFIG.get("base_url", "")).path.rstrip("/")


# ---------------------------------------------------------------- markdown --

def md_inline(text: str) -> str:
    """Escape HTML, then apply inline code and bold. Leaves math untouched."""
    out = []
    # Split out `code` spans first so nothing inside them is processed.
    parts = re.split(r"(`[^`]+`)", text)
    for part in parts:
        if part.startswith("`") and part.endswith("`") and len(part) > 2:
            out.append("<code>" + html.escape(part[1:-1]) + "</code>")
        else:
            escaped = html.escape(part, quote=False)
            escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
            out.append(escaped)
    return "".join(out)


def md_to_html(md: str) -> str:
    lines = md.split("\n")
    out = []
    para: list[str] = []
    in_code = False
    code_lang = ""
    code_lines: list[str] = []
    list_type = None  # None | "ul" | "ol"

    def flush_para():
        if para:
            out.append("<p>" + md_inline(" ".join(para)) + "</p>")
            para.clear()

    def close_list():
        nonlocal list_type
        if list_type:
            out.append(f"</{list_type}>")
            list_type = None

    for line in lines:
        if in_code:
            if line.strip().startswith("```"):
                cls = f' class="language-{code_lang}"' if code_lang else ""
                out.append(f"<pre><code{cls}>" + html.escape("\n".join(code_lines)) + "</code></pre>")
                in_code = False
                code_lines = []
            else:
                code_lines.append(line)
            continue

        stripped = line.strip()
        if stripped.startswith("```"):
            flush_para()
            close_list()
            in_code = True
            code_lang = stripped[3:].strip()
            continue

        m = re.match(r"^(#{2,4})\s+(.*)$", stripped)
        if m:
            flush_para()
            close_list()
            level = len(m.group(1))
            out.append(f"<h{level}>{md_inline(m.group(2))}</h{level}>")
            continue

        m = re.match(r"^[-*]\s+(.*)$", stripped)
        if m:
            flush_para()
            if list_type != "ul":
                close_list()
                out.append("<ul>")
                list_type = "ul"
            out.append("<li>" + md_inline(m.group(1)) + "</li>")
            continue

        m = re.match(r"^\d+[.)]\s+(.*)$", stripped)
        if m:
            flush_para()
            if list_type != "ol":
                close_list()
                out.append("<ol>")
                list_type = "ol"
            out.append("<li>" + md_inline(m.group(1)) + "</li>")
            continue

        if not stripped:
            flush_para()
            close_list()
            continue

        # Display math lines pass through raw (MathJax handles them).
        if stripped.startswith("$$") or para == [] and stripped.endswith("$$") and "$$" in stripped:
            flush_para()
            close_list()
            out.append(stripped)
            continue

        para.append(stripped)

    flush_para()
    close_list()
    return "\n".join(out)


# ----------------------------------------------------------------- content --

def parse_question(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", raw, re.DOTALL)
    if not m:
        sys.exit(f"ERROR: {path} is missing frontmatter")
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    body = m.group(2)

    required = ["title", "subject", "topic", "level", "difficulty", "description", "date"]
    missing = [k for k in required if not meta.get(k)]
    if missing:
        sys.exit(f"ERROR: {path} missing frontmatter keys: {missing}")
    if meta["subject"] not in CONFIG["subjects"]:
        sys.exit(f"ERROR: {path} has unknown subject '{meta['subject']}'")

    sections = {}
    for name, text in re.findall(r"^##\s+(\w+)\s*\n(.*?)(?=^##\s+\w+\s*$|\Z)", body, re.DOTALL | re.MULTILINE):
        sections[name.lower()] = text.strip()
    for req in ("question", "solution", "answer"):
        if req not in sections:
            sys.exit(f"ERROR: {path} missing '## {req.title()}' section")

    meta["slug"] = path.stem
    meta["sections"] = sections
    return meta


# --------------------------------------------------------------- templates --

CSS = """
:root { --bg:#ffffff; --fg:#1a1d21; --muted:#5b6470; --card:#f5f6f8; --accent:#0b6e4f;
        --accent-fg:#ffffff; --border:#e2e5e9; --code:#f0f1f3; }
@media (prefers-color-scheme: dark) {
  :root { --bg:#15181c; --fg:#e8eaed; --muted:#9aa3ad; --card:#1e2228; --accent:#3ecf8e;
          --accent-fg:#0c2b1f; --border:#2c313a; --code:#23272e; }
}
* { box-sizing: border-box; }
body { margin:0; font-family: Georgia, 'Times New Roman', serif; background:var(--bg);
       color:var(--fg); line-height:1.65; }
header { border-bottom:1px solid var(--border); }
.wrap { max-width: 760px; margin: 0 auto; padding: 0 1.25rem; }
header .wrap { display:flex; align-items:baseline; gap:1rem; flex-wrap:wrap; padding-top:1rem; padding-bottom:1rem; }
.brand { font-weight:bold; font-size:1.15rem; color:var(--fg); text-decoration:none; }
nav a { color:var(--muted); text-decoration:none; margin-right:.85rem; font-size:.92rem;
        font-family: system-ui, sans-serif; }
nav a:hover { color:var(--accent); }
main { padding: 2rem 0 3rem; }
h1 { font-size:1.7rem; line-height:1.3; margin:.2rem 0 1rem; }
h2 { font-size:1.25rem; margin-top:2rem; }
a { color: var(--accent); }
.meta { font-family: system-ui, sans-serif; font-size:.85rem; color:var(--muted); margin-bottom:1.5rem; }
.meta span { margin-right:1rem; }
.card { background:var(--card); border:1px solid var(--border); border-radius:10px;
        padding:1rem 1.25rem; margin:.8rem 0; }
.card a.title { font-size:1.05rem; text-decoration:none; color:var(--fg); font-weight:bold; }
.card a.title:hover { color:var(--accent); }
.card .sub { font-family: system-ui, sans-serif; font-size:.82rem; color:var(--muted); margin-top:.25rem; }
details.solution { border:1px solid var(--border); border-radius:10px; padding:0; margin:1.5rem 0; }
details.solution summary { cursor:pointer; padding:.9rem 1.25rem; font-family:system-ui,sans-serif;
        font-weight:600; color:var(--accent); }
details.solution > div { padding:0 1.25rem 1rem; border-top:1px solid var(--border); }
pre { background:var(--code); border:1px solid var(--border); border-radius:8px; padding:1rem;
      overflow-x:auto; font-size:.9rem; line-height:1.5; }
code { background:var(--code); border-radius:4px; padding:.1em .35em; font-size:.92em; }
pre code { background:none; padding:0; }
footer { border-top:1px solid var(--border); padding:1.5rem 0 2.5rem; font-family:system-ui,sans-serif;
         font-size:.85rem; color:var(--muted); }
.subject-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(230px,1fr)); gap:.9rem; }
.pill { display:inline-block; font-family:system-ui,sans-serif; font-size:.75rem; border:1px solid var(--border);
        border-radius:999px; padding:.1rem .6rem; color:var(--muted); }
.crumbs { font-family:system-ui,sans-serif; font-size:.85rem; color:var(--muted); margin-bottom:.4rem; }
.crumbs a { color:var(--muted); }
img { max-width:100%; }
table { border-collapse:collapse; } td,th { border:1px solid var(--border); padding:.4rem .7rem; }
"""

MATHJAX = (
    '<script>window.MathJax={tex:{inlineMath:[["\\\\(","\\\\)"]],displayMath:[["$$","$$"]]}};</script>\n'
    '<script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>'
)


def page(title: str, description: str, body: str, canonical: str = "", extra_head: str = "") -> str:
    site = CONFIG["site_name"]
    nav = " ".join(
        f'<a href="{PREFIX}/{slug}/">{html.escape(info["name"])}</a>'
        for slug, info in CONFIG["subjects"].items()
    )
    canonical_tag = ""
    base = CONFIG.get("base_url", "").rstrip("/")
    if base and canonical:
        canonical_tag = f'<link rel="canonical" href="{base}{canonical}">'
    analytics = CONFIG.get("analytics_snippet", "")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} | {html.escape(site)}</title>
<meta name="description" content="{html.escape(description)}">
{canonical_tag}
<style>{CSS}</style>
{MATHJAX}
{extra_head}
</head>
<body>
<header><div class="wrap">
  <a class="brand" href="{PREFIX}/">{html.escape(site)}</a>
  <nav>{nav}</nav>
</div></header>
<main><div class="wrap">
{body}
</div></main>
<footer><div class="wrap">
  {html.escape(CONFIG["tagline"])}. Updated daily.
</div></footer>
{analytics}
</body>
</html>"""


def question_page(q: dict) -> str:
    s = CONFIG["subjects"][q["subject"]]
    body_parts = [
        f'<div class="crumbs"><a href="{PREFIX}/">Home</a> › <a href="{PREFIX}/{q["subject"]}/">{html.escape(s["name"])}</a> › {html.escape(q["topic"])}</div>',
        f"<h1>{html.escape(q['title'])}</h1>",
        f'<div class="meta"><span>📚 {html.escape(s["name"])}</span><span>🧩 {html.escape(q["topic"])}</span>'
        f'<span>🎯 {html.escape(q["difficulty"])}</span><span>🎓 {html.escape(q["level"])}</span></div>',
        "<h2>Question</h2>",
        md_to_html(q["sections"]["question"]),
        '<details class="solution"><summary>Show worked solution</summary><div>',
        md_to_html(q["sections"]["solution"]),
        "</div></details>",
        '<details class="solution"><summary>Show final answer</summary><div>',
        md_to_html(q["sections"]["answer"]),
        "</div></details>",
    ]
    support = CONFIG.get("support_link", "")
    if support:
        body_parts.append(
            f'<p class="meta">Found this useful? <a href="{support}">Support the site</a> to unlock topic packs.</p>'
        )
    jsonld = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": q["title"],
        "description": q["description"],
        "datePublished": q["date"],
        "about": f'{s["name"]} — {q["topic"]}',
    }
    extra = f'<script type="application/ld+json">{json.dumps(jsonld)}</script>'
    return page(q["title"], q["description"], "\n".join(body_parts),
                canonical=f"/{q['subject']}/{q['slug']}.html", extra_head=extra)


def subject_page(slug: str, questions: list[dict]) -> str:
    s = CONFIG["subjects"][slug]
    by_topic: dict[str, list[dict]] = {}
    for q in questions:
        by_topic.setdefault(q["topic"], []).append(q)
    parts = [f"<h1>{html.escape(s['name'])} Practice Questions</h1>",
             f"<p>{html.escape(s['blurb'])}</p>"]
    for topic in sorted(by_topic):
        parts.append(f"<h2>{html.escape(topic)}</h2>")
        for q in sorted(by_topic[topic], key=lambda x: x["date"], reverse=True):
            parts.append(
                f'<div class="card"><a class="title" href="{PREFIX}/{slug}/{q["slug"]}.html">{html.escape(q["title"])}</a>'
                f'<div class="sub">{html.escape(q["difficulty"])} · {html.escape(q["level"])} · {html.escape(q["date"])}</div></div>'
            )
    return page(f"{s['name']} Practice Questions", s["blurb"], "\n".join(parts), canonical=f"/{slug}/")


def home_page(questions: list[dict]) -> str:
    parts = [f"<h1>{html.escape(CONFIG['tagline'])}</h1>",
             "<p>New questions added every day, each with a full step-by-step worked solution. "
             "Built for the Singapore syllabus: O-Levels, A-Levels, poly and university modules.</p>",
             '<div class="subject-grid">']
    counts: dict[str, int] = {}
    for q in questions:
        counts[q["subject"]] = counts.get(q["subject"], 0) + 1
    for slug, info in CONFIG["subjects"].items():
        n = counts.get(slug, 0)
        parts.append(
            f'<div class="card"><a class="title" href="{PREFIX}/{slug}/">{html.escape(info["name"])}</a>'
            f'<div class="sub">{n} question{"s" if n != 1 else ""}</div></div>'
        )
    parts.append("</div>")
    latest = sorted(questions, key=lambda x: x["date"], reverse=True)[:8]
    if latest:
        parts.append("<h2>Latest questions</h2>")
        for q in latest:
            s = CONFIG["subjects"][q["subject"]]
            parts.append(
                f'<div class="card"><a class="title" href="{PREFIX}/{q["subject"]}/{q["slug"]}.html">{html.escape(q["title"])}</a>'
                f'<div class="sub">{html.escape(s["name"])} · {html.escape(q["topic"])} · {html.escape(q["date"])}</div></div>'
            )
    return page("Home", CONFIG["tagline"], "\n".join(parts), canonical="/")


# ------------------------------------------------------------------- build --

def main() -> None:
    questions = [parse_question(p) for p in sorted(CONTENT.rglob("*.md"))]
    slugs = [f'{q["subject"]}/{q["slug"]}' for q in questions]
    dupes = {s for s in slugs if slugs.count(s) > 1}
    if dupes:
        sys.exit(f"ERROR: duplicate question slugs: {dupes}")

    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()

    (DIST / "index.html").write_text(home_page(questions), encoding="utf-8")
    urls = ["/"]

    for slug in CONFIG["subjects"]:
        subject_qs = [q for q in questions if q["subject"] == slug]
        d = DIST / slug
        d.mkdir()
        (d / "index.html").write_text(subject_page(slug, subject_qs), encoding="utf-8")
        urls.append(f"/{slug}/")
        for q in subject_qs:
            (d / f'{q["slug"]}.html').write_text(question_page(q), encoding="utf-8")
            urls.append(f'/{slug}/{q["slug"]}.html')

    base = CONFIG.get("base_url", "").rstrip("/")
    if base:
        sitemap = ['<?xml version="1.0" encoding="UTF-8"?>',
                   '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
        for u in urls:
            sitemap.append(f"  <url><loc>{base}{u}</loc></url>")
        sitemap.append("</urlset>")
        (DIST / "sitemap.xml").write_text("\n".join(sitemap), encoding="utf-8")
        (DIST / "robots.txt").write_text(
            f"User-agent: *\nAllow: /\nSitemap: {base}/sitemap.xml\n", encoding="utf-8")
    else:
        (DIST / "robots.txt").write_text("User-agent: *\nAllow: /\n", encoding="utf-8")

    # Machine-readable index — the daily generation routine reads this to see
    # existing coverage and avoid duplicates.
    index = [{k: q[k] for k in ("title", "subject", "topic", "level", "difficulty", "date", "slug")}
             for q in questions]
    (ROOT / "data" / "index.json").write_text(json.dumps(index, indent=2), encoding="utf-8")

    print(f"Built {len(questions)} questions across "
          f"{len({q['subject'] for q in questions})} subjects -> {DIST}")


if __name__ == "__main__":
    main()
