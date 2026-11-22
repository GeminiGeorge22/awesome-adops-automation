#!/usr/bin/env python3
"""Local checker for README.md format.

Validates:
  1. every entry line matches the required format
     `![icon](image/alg_R.png) [Name](https://url) - description`
     (github icon -> alg_R.png, web icon -> alg_I.png)
  2. every referenced image exists on disk
  3. every Table of Contents anchor matches the generated anchor for an H2 heading
  4. entry URLs do not use common search or redirect endpoints

The URL check is heuristic; contributors should still verify links manually.
Exits 0 when everything passes, 1 otherwise.
"""
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

README = Path(__file__).resolve().parent.parent / "README.md"
ROOT = README.parent

ICON_RE = re.compile(
    r"^!\[(?P<icon>github|web)\]\((?P<image>image/alg_[RI]\.png)\)\s+"
    r"\[(?P<name>[^\]]+)\]\((?P<url>https?://[^)\s]+)\)\s+-\s+(?P<description>.+)$"
)
TOC_LINK_RE = re.compile(r"^-\s+\[(.+?)\]\(#([^)]+)\)\s*$", re.MULTILINE)
HEADING_RE = re.compile(r"^(#{1,2})\s+(.*)$", re.MULTILINE)

# Check actual redirect/search endpoints rather than words in resource names or
# arbitrary paths (e.g. Search Ads 360 or a project called redirect-checker).
SHORTENER_HOSTS = {
    "bit.ly", "buff.ly", "goo.gl", "l.facebook.com", "lnkd.in", "ow.ly",
    "t.co", "tinyurl.com",
}
SEARCH_OR_REDIRECT_PATHS = {
    "google.com": {"/search", "/url", "/imgres", "/goto"},
    "www.google.com": {"/search", "/url", "/imgres", "/goto"},
    "bing.com": {"/search"},
    "www.bing.com": {"/search"},
    "duckduckgo.com": {"", "/l"},
    "www.duckduckgo.com": {"", "/l"},
    "search.yahoo.com": {"", "/search"},
    "search.brave.com": {"", "/search"},
}

failures = []


def is_indirect_url(url):
    """Recognize common search and redirect URLs without blocking direct links."""
    parts = urlsplit(url)
    if not parts.hostname:
        raise ValueError("URL must include a hostname")
    host = parts.hostname.lower().rstrip(".")
    path = parts.path.lower().rstrip("/")
    if host in SHORTENER_HOSTS or (host.startswith("www.") and host[4:] in SHORTENER_HOSTS):
        return True
    return path in SEARCH_OR_REDIRECT_PATHS.get(host, set())


def anchor(heading):
    a = heading.strip().lower()
    a = "".join(c for c in a if c.isalnum() or c in ("-", " "))
    a = a.replace(" ", "-")
    return a.strip("-")


def main():
    failures.clear()
    if not README.exists():
        failures.append(f"README.md not found at {README}")
        print_failures()
        return 1

    text = README.read_text(encoding="utf-8")
    lines = text.splitlines()

    # 1. entry format
    entries = 0
    for i, line in enumerate(lines, 1):
        if line.strip().startswith("!["):
            entries += 1
            m = ICON_RE.match(line.strip())
            if not m:
                failures.append(f"line {i}: entry line does not match the required format")
                continue
            icon = m.group("icon")
            image = m.group("image")
            url = m.group("url")
            desc = m.group("description")
            if icon == "github" and image != "image/alg_R.png":
                failures.append(f"line {i}: github icon must use image/alg_R.png, got {image}")
            if icon == "web" and image != "image/alg_I.png":
                failures.append(f"line {i}: web icon must use image/alg_I.png, got {image}")
            try:
                if is_indirect_url(url):
                    failures.append(f"line {i}: link looks like a search/redirect service: {url}")
            except ValueError:
                failures.append(f"line {i}: invalid link URL: {url}")
            if len(desc) < 10:
                failures.append(f"line {i}: description looks too short")

    # 2. image references
    for match in re.finditer(r"!\[[^\]]*\]\(([^)]+)\)", text):
        src = match.group(1).split()[0] if match.group(1).split() else match.group(1)
        if src.startswith(("http://", "https://")):
            continue
        if not (ROOT / src).exists():
            failures.append(f"referenced image missing: {src}")

    # 3. TOC anchors
    headings = {}
    for m in HEADING_RE.finditer(text):
        level = len(m.group(1))
        if level == 2:
            headings[anchor(m.group(2))] = m.group(2)
    for m in TOC_LINK_RE.finditer(text):
        label, target = m.group(1), m.group(2)
        if target not in headings:
            failures.append(f"TOC entry '{label}' points to missing heading anchor '#{target}'")

    if entries == 0:
        failures.append("no entries found (no lines starting with ![github] or ![web])")

    print(f"checked {entries} entries, {len(headings)} sections")
    print_failures()
    return 1 if failures else 0


def print_failures():
    if failures:
        print("\n✖ Problems found:")
        for f in failures:
            print(f"  - {f}")
    else:
        print("✓ README format check passed")


if __name__ == "__main__":
    sys.exit(main())
