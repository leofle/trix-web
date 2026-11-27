#!/usr/bin/env python3
"""Refresh index.html's built-in copy of the latest trix releases.

The page fetches the version and "What's new" from GitHub when it loads, but
crawlers that don't run JavaScript, and visitors whose request to GitHub fails,
see the copy written into the HTML. This rewrites that copy from GitHub's
releases, with the same rules the page's own script uses, so both agree.

The Pages workflow runs it before every deploy. To run it by hand:

    python3 scripts/refresh-releases.py            # rewrites index.html
    python3 scripts/refresh-releases.py page.html  # or another file

It reads GITHUB_TOKEN from the environment if set, for a higher API limit.
"""
import html
import json
import os
import re
import sys
import urllib.request
from datetime import datetime

API = "https://api.github.com/repos/leofle/trix/releases?per_page=10"

# The same rules as the page's script (see "version and what's new" in index.html).
NOISE = re.compile(r"^Version \d|\btests?\b|\bCI\b", re.I)
LINE = re.compile(r"^[*-] (?!@)(.+?)(?: by @[\w-]+)?(?: in (https://github\.com/[\w./-]+/pull/(\d+)))?\s*$")


def fetch():
    req = urllib.request.Request(API, headers={"Accept": "application/vnd.github+json"})
    if os.environ.get("GITHUB_TOKEN"):
        req.add_header("Authorization", "Bearer " + os.environ["GITHUB_TOKEN"])
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def esc(s):
    return html.escape(s, quote=False)


def attr(s):
    return html.escape(s, quote=True).replace("&#x27;", "'")


def day(iso):
    d = datetime.strptime(iso, "%Y-%m-%dT%H:%M:%SZ")
    return f"{d:%b} {d.day}, {d.year}"


def changes(body):
    out = []
    for line in re.split(r"^## New Contributors", body or "", flags=re.M)[0].split("\n"):
        m = LINE.match(line.rstrip("\r"))
        if m and not NOISE.search(m[1]):
            out.append(m)
    return out


def render(rels):
    latest = rels[0]["tag_name"]
    shown = [(r, c) for r in rels if (c := changes(r["body"]))][:3]
    blocks = []
    for r, items in shown:
        lis = "\n".join(
            f'          <li><a href="{attr(m[2])}">{esc(m[1])} <span class="pr">#{m[3]}</span></a></li>'
            if m[2] else f"          <li>{esc(m[1])}</li>"
            for m in items)
        is_latest = r["tag_name"] == latest
        pill = '<span class="pill">latest</span>' if is_latest else ""
        blocks.append(
            f'      <div class="rel{" latest" if is_latest else ""}">\n'
            f'        <div><a class="tag" href="{attr(r["html_url"])}">{esc(r["tag_name"])}</a>'
            f'<span class="when">{day(r["published_at"])}</span>'
            f"{pill}</div>\n"
            f"        <ul>\n{lis}\n        </ul>\n"
            f"      </div>")
    return "\n".join(blocks)


def main():
    page = sys.argv[1] if len(sys.argv) > 1 else "index.html"
    rels = [r for r in fetch() if not r["draft"]]
    if not rels:
        sys.exit("no releases found")
    latest = rels[0]

    src = open(page, encoding="utf-8").read()
    new, n = re.subn(r'(<div class="rels" id="rels">\n).*?(\n    </div>\n  </section>)',
                     lambda m: m[1] + render(rels) + m[2], src, count=1, flags=re.S)
    if n != 1:
        sys.exit("couldn't find the releases list in " + page)
    new = re.sub(r"(data-version>)v[\w.-]+(<)", lambda m: m[1] + latest["tag_name"] + m[2], new)
    new = re.sub(r"(data-version-date>)\([^)]*\)(<)", lambda m: f'{m[1]}({day(latest["published_at"])}){m[2]}', new)

    if new == src:
        print(f"{page} already shows {latest['tag_name']}")
    else:
        open(page, "w", encoding="utf-8").write(new)
        print(f"{page} now shows {latest['tag_name']} ({day(latest['published_at'])})")


if __name__ == "__main__":
    main()
