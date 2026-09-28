#!/usr/bin/env python3
"""Structural checks for Persian skill packages and sample outputs."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CLICHES = [
    "در دنیای امروز",
    "لازم به ذکر است",
    "همان‌طور که می‌دانیم",
    "در نهایت می‌توان گفت",
    "در عصر دیجیتال",
    "شایان ذکر است",
]

BAD_SPACING = [
    (r"می[ ]توان", "می توان → می‌توان"),
    (r"می[ ]شود", "می شود → می‌شود"),
    (r"نمی[ ]توان", "نمی توان → نمی‌توان"),
    (r"(?<![=\w])به صورت(?!\w)", "به صورت → به‌صورت"),
    (r"(?<![=\w])به عنوان(?!\w)", "به عنوان → به‌عنوان"),
]

TECH_NAMES_SKILL1 = ["TaskFlow", "Redis", "Docker", "Linux"]


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    raise SystemExit(1)


def ok(msg: str) -> None:
    print(f"OK: {msg}")


def check_skill_frontmatter(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(f"{path}: missing YAML frontmatter")
    body = text.split("---", 2)[1]
    if "name:" not in body:
        fail(f"{path}: missing name in frontmatter")
    if "description:" not in body:
        fail(f"{path}: missing description in frontmatter")
    lines = text.count("\n") + 1
    if lines > 500:
        fail(f"{path}: SKILL.md has {lines} lines (max 500)")
    ok(f"{path.relative_to(ROOT)} frontmatter + length ({lines} lines)")


def check_no_cliches(label: str, text: str) -> None:
    for c in CLICHES:
        if c in text:
            fail(f"{label}: contains cliché «{c}»")
    ok(f"{label}: no banned clichés")


def check_spacing(label: str, text: str) -> None:
    for pattern, hint in BAD_SPACING:
        if re.search(pattern, text):
            fail(f"{label}: bad spacing ({hint})")
    ok(f"{label}: spacing heuristics passed")


def check_tech_names(label: str, text: str, names: list[str]) -> None:
    for name in names:
        if name not in text:
            fail(f"{label}: missing technical name {name}")
    ok(f"{label}: technical names present")


def main() -> None:
    skill1 = ROOT / "persian-writing-mastery" / "SKILL.md"
    skill2 = ROOT / "natural-persian-text-editor" / "SKILL.md"
    for p in (skill1, skill2):
        if not p.exists():
            fail(f"missing {p}")
        check_skill_frontmatter(p)

    for rel in (
        "persian-writing-mastery/grammar-reference.md",
        "persian-writing-mastery/examples.md",
        "natural-persian-text-editor/quality-signals.md",
        "natural-persian-text-editor/examples.md",
        "tests/samples/skill1-prompt.md",
        "tests/samples/skill2-input.md",
        "tests/expected/skill1-output.md",
        "tests/expected/skill2-output.md",
        "README.md",
        "assets/banner.png",
    ):
        path = ROOT / rel
        if not path.exists():
            fail(f"missing {rel}")
        ok(f"exists {rel}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "assets/banner.png" not in readme:
        fail("README.md must reference assets/banner.png")
    ok("README.md links banner")

    out1 = (ROOT / "tests/expected/skill1-output.md").read_text(encoding="utf-8")
    out2 = (ROOT / "tests/expected/skill2-output.md").read_text(encoding="utf-8")

    check_tech_names("skill1 output", out1, TECH_NAMES_SKILL1)
    check_no_cliches("skill1 output", out1.split("## بررسی")[0])
    check_spacing("skill1 output", out1.split("## بررسی")[0])

    check_no_cliches("skill2 output", out2.split("## تغییرات")[0])
    check_spacing("skill2 output", out2.split("## تغییرات")[0])
    if "Cursor" not in out2:
        fail("skill2 output: missing Cursor")
    ok("skill2 output: Cursor preserved")

    skill2_text = skill2.read_text(encoding="utf-8")
    if "AI Detector" not in skill2_text and "آشکارساز" not in skill2_text:
        fail("skill2 SKILL.md should mention detector prohibition")
    ok("skill2 SKILL.md includes detector prohibition")

    print("\nAll checks passed.")


if __name__ == "__main__":
    main()
