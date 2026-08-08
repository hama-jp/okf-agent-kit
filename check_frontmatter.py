#!/usr/bin/env python3
"""OKF v0.2語彙のfrontmatter最小チェッカー (AI不使用の決定論チェック)。

仕様のattester(検査はLLMなしの決定論コードで行う)の発想を、
frontmatterの整合チェックに最小限だけ借りたもの。usage:
    python3 check_frontmatter.py <dir> [<dir>...]
"""
import datetime
import re
import sys
from pathlib import Path

TODAY = datetime.date.today()
STATUS_VALUES = {"draft", "stable", "deprecated"}
ACTOR_RE = re.compile(r"^(human:\S+|process:\S+|[\w.-]+/[\w.-]+)$")


def parse_frontmatter(text: str):
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end < 0:
        return None
    fm = {}
    for line in text[3:end].splitlines():
        m = re.match(r"^(\w+):\s*(.*)$", line)
        if m:
            fm[m.group(1)] = m.group(2).split("#")[0].strip()
    return fm


def check_file(path: Path):
    issues = []
    fm = parse_frontmatter(path.read_text(encoding="utf-8"))
    if fm is None:
        return ["frontmatter がない"]
    if not fm.get("type"):
        issues.append("type がない (唯一の必須キー)")
    gen = fm.get("generated", "")
    m = re.search(r"by:\s*([^,}]+)", gen)
    if not m:
        issues.append("generated.by がない")
    elif not ACTOR_RE.match(m.group(1).strip()):
        issues.append(f"generated.by の表記が規約外: {m.group(1).strip()}")
    status = fm.get("status", "")
    if status and status not in STATUS_VALUES:
        issues.append(f"status が想定外: {status}")
    stale = fm.get("stale_after", "").strip('"')
    if stale and stale != "null":
        try:
            if datetime.date.fromisoformat(stale) <= TODAY:
                issues.append(f"stale_after 超過 ({stale}) — 要再確認")
        except ValueError:
            issues.append(f"stale_after が日付でない: {stale}")
    return issues


def main():
    ok = True
    for d in sys.argv[1:]:
        for path in sorted(Path(d).glob("*.md")):
            if path.name in ("MEMORY.md", "index.md"):  # 目次は対象外
                continue
            issues = check_file(path)
            mark = "✅" if not issues else "🔴"
            print(f"{mark} {path}")
            for i in issues:
                ok = False
                print(f"     - {i}")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
