#!/usr/bin/env python3
"""Local checker for README.md format.

Validates:
  1. every entry line matches the required format
     `![icon](image/alg_R.png) [Name](https://url) - description`
     (github icon -> alg_R.png, web icon -> alg_I.png)
  2. every referenced image exists on disk
  3. every Table of Contents anchor matches the generated anchor for an H2/H1 heading

Exits 0 when everything passes, 1 otherwise.
"""
import re
import sys
from pathlib import Path

README = Path(__file__).resolve().parent.parent / "README.md"
ROOT = README.parent

ICON_RE = re.compile(
    r"^(!\[(github|web)\]\((image/alg_[RI]\.png)\))\s+(\[.+?\]\(https?://[^)\s]+\))\s+-\s+(.+)$"
)
TOC_LINK_RE = re.compile(r"^-\s+\[(.+?)\]\(#([^)]+)\)\s*$", re.MULTILINE)
HEADING_RE = re.compile(r"^(#{1,2})\s+(.*)$", re.MULTILINE)

failures = []


def anchor(heading):
    a = heading.strip().lower()
    a = "".join(c for c in a if c.isalnum() or c in ("-", " "))
    a = a.replace(" ", "-")
    return a.strip("-")


def main():
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
            icon, image, link, desc = m.group(2), m.group(3), m.group(4), m.group(5)
            if icon == "github" and image != "image/alg_R.png":
                failures.append(f"line {i}: github icon must use image/alg_R.png, got {image}")
            if icon == "web" and image != "image/alg_I.png":
                failures.append(f"line {i}: web icon must use image/alg_I.png, got {image}")
            if "search" in link.lower() or "redirect" in link.lower():
                failures.append(f"line {i}: link looks like a search/redirect service: {link}")
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
