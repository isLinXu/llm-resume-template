#!/usr/bin/env python3
"""Generate the browser editor registry from the real LaTeX entry files."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LATEX_DIR = ROOT / "latex_resume_pro"
OUTPUT = ROOT / "docs" / "variant-sources.js"

VARIANTS = [
    ("main", "中文主简历", "📄", "默认完整版", "resume-pro-zh.tex", "resume-pro-zh.pdf"),
    ("academic", "学术灰", "🎓", "科研 / 申博", "variants/variant-academic.tex", "variant-academic.pdf"),
    ("academic-long", "学术长版", "📚", "完整学术 CV", "variants/variant-academic-long.tex", "variant-academic-long.pdf"),
    ("blackpro", "商务黑", "💼", "管理 / 金融", "variants/variant-blackpro.tex", "variant-blackpro.pdf"),
    ("product", "活力橙", "🚀", "产品 / 创业", "variants/variant-product.tex", "variant-product.pdf"),
    ("minimalist", "极简单色", "✨", "ATS / 黑白打印", "variants/variant-minimalist.tex", "variant-minimalist.pdf"),
    ("onepage", "一页紧凑", "📋", "校招 / 应届", "variants/variant-onepage.tex", "variant-onepage.pdf"),
    ("english", "英文版", "🌍", "海外 / 外企", "variants/variant-english.tex", "variant-english.pdf"),
    ("purple", "专业紫", "💜", "创意 / 媒体", "variants/variant-purple.tex", "variant-purple.pdf"),
    ("twocolumn", "双栏", "📰", "快速浏览", "variants/variant-twocolumn.tex", "variant-twocolumn.pdf"),
    ("coverletter", "求职信", "✉️", "配套信件", "variants/variant-coverletter.tex", "variant-coverletter.pdf"),
]


def build_registry() -> list[dict[str, object]]:
    registry = []
    for variant_id, name, icon, description, relative_path, pdf in VARIANTS:
        path = LATEX_DIR / relative_path
        source = path.read_text(encoding="utf-8")
        class_match = re.search(r"\\documentclass\[([^]]*)\]\{resume-pro\}", source)
        if not class_match:
            raise ValueError(f"Cannot read resume-pro class options: {path}")
        theme_match = re.search(r"^\\settheme\{([^}]+)\}", source, re.MULTILINE)
        registry.append(
            {
                "id": variant_id,
                "name": name,
                "icon": icon,
                "desc": description,
                "theme": theme_match.group(1) if theme_match else "techblue",
                "opts": class_match.group(1),
                "path": f"latex_resume_pro/{relative_path}",
                "entry": Path(relative_path).name,
                "pdf": pdf,
                "content": "modules-en" if variant_id == "english" else "modules",
                "source": source,
            }
        )
    return registry


def render() -> str:
    registry = json.dumps(build_registry(), ensure_ascii=False, indent=2)
    return (
        "// 此文件由 latex_resume_pro/scripts/generate_editor_variants.py 自动生成，请勿手改。\n"
        "// 变体名称、编译选项、目标路径与 entry 源码均以真实 LaTeX 文件为准。\n"
        f"window.RESUME_VARIANTS = Object.freeze({registry});\n"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail when the generated file is stale")
    args = parser.parse_args()
    content = render()
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != content:
            print(f"Outdated: {OUTPUT}. Run latex_resume_pro/scripts/generate_editor_variants.py")
            return 1
        print(f"Editor variant registry is up to date: {OUTPUT}")
        return 0
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(content, encoding="utf-8")
    print(f"Generated {len(VARIANTS)} variants: {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
