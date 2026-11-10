#!/usr/bin/env python3
"""Synchronize user-facing version labels from VERSION, or check them with --check."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def replace_pattern(text: str, pattern: str, replacement: str, label: str, errors: list[str]) -> str:
    updated, count = re.subn(pattern, replacement, text)
    if count == 0:
        errors.append(f"{label}: no version marker matched")
    return updated


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="report drift without modifying files")
    args = parser.parse_args()

    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        print(f"Invalid VERSION: {version!r}", file=sys.stderr)
        return 1

    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    release = re.search(rf"^## \[{re.escape(version)}\] - (\d{{4}})-(\d{{2}})-(\d{{2}})$", changelog, re.M)
    if not release:
        print(f"CHANGELOG.md has no dated entry for {version}", file=sys.stderr)
        return 1
    latex_date = "/".join(release.groups())

    package_path = ROOT / "package.json"
    package = json.loads(package_path.read_text(encoding="utf-8"))
    package_text = None
    if package.get("version") != version:
        package["version"] = version
        package_text = json.dumps(package, ensure_ascii=False, indent=2) + "\n"

    targets: dict[Path, str | None] = {package_path: package_text}
    errors: list[str] = []

    rules = [
        ("docs/index.html", r"v\d+\.\d+\.\d+", f"v{version}"),
        ("docs/editor.html", r"v\d+\.\d+\.\d+", f"v{version}"),
        ("docs/sw.js", r"v\d+\.\d+\.\d+", f"v{version}"),
        ("latex_resume_pro/README.md", r"v\d+\.\d+\.\d+", f"v{version}"),
    ]
    for relative, pattern, replacement in rules:
        path = ROOT / relative
        original = path.read_text(encoding="utf-8")
        updated = replace_pattern(original, pattern, replacement, relative, errors)
        targets[path] = updated if updated != original else None

    cls_path = ROOT / "latex_resume_pro/resume-pro.cls"
    cls_original = cls_path.read_text(encoding="utf-8")
    cls_updated = replace_pattern(
        cls_original, r"v\d+\.\d+\.\d+", f"v{version}", "latex_resume_pro/resume-pro.cls", errors
    )
    cls_updated = replace_pattern(
        cls_updated,
        r"(\\ProvidesClass\{resume-pro\}\[)\d{4}/\d{2}/\d{2}",
        rf"\g<1>{latex_date}",
        "latex_resume_pro/resume-pro.cls class date",
        errors,
    )
    targets[cls_path] = cls_updated if cls_updated != cls_original else None

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    changed = [path for path, content in targets.items() if content is not None]
    if args.check:
        if changed:
            for path in changed:
                print(f"OUT OF SYNC: {path.relative_to(ROOT)}")
            return 1
        print(f"All version labels are synchronized: v{version}")
        return 0

    for path in changed:
        path.write_text(targets[path] or "", encoding="utf-8")
        print(f"Updated {path.relative_to(ROOT)}")
    print(f"Version labels synchronized: v{version}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
