#!/usr/bin/env python3
"""
build_placeholders.py
---------------------
Generate placeholder Logo PNG/SVG for the resume template.
Real logos can simply overwrite the same-named files.

Usage:
    python3 build_placeholders.py              # generate PNG (default)
    python3 build_placeholders.py --svg         # also generate SVG
    python3 build_placeholders.py --only svg    # SVG only
    python3 build_placeholders.py --size 512    # custom size (default 256)
    python3 build_placeholders.py --output ./out # custom output dir

Cross-platform: macOS / Linux / Windows font auto-detection.
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
from platform import system as _sys
import argparse
import os
import sys

# ---------------------------------------------------------------------------
# Logo definitions: (filename_stem, bg_hex, fg_hex, label)
# ---------------------------------------------------------------------------
LOGOS = [
    # ---- 中国高校 ----
    ("tsinghua.png",   "#4B0082", "#FFFFFF", "清华"),
    ("peking.png",     "#9F1239", "#FFFFFF", "北大"),
    ("pku.png",        "#1A3C6F", "#FFFFFF", "PKU"),
    ("sjtu.png",       "#A62732", "#FFFFFF", "SJTU"),
    ("zju.png",        "#003F88", "#FFFFFF", "ZJU"),
    ("fudan.png",      "#003C9D", "#FFFFFF", "FDU"),
    ("ustc.png",       "#0070BB", "#FFFFFF", "USTC"),
    ("cas.png",        "#1F5AA6", "#FFFFFF", "CAS"),
    ("hit.png",        "#003366", "#FFFFFF", "HIT"),
    ("nju.png",        "#660066", "#FFFFFF", "NJU"),
    ("whu.png",        "#003399", "#FFFFFF", "武大"),
    ("hust.png",       "#A42121", "#FFFFFF", "华科"),
    ("sysu.png",       "#006633", "#FFFFFF", "中大"),
    ("ruc.png",        "#8B0000", "#FFFFFF", "人大"),
    ("cug.png",        "#0066CC", "#FFFFFF", "地大"),
    ("swjtu.png",      "#003399", "#FFFFFF", "西南交大"),
    ("scu.png",        "#1B4D9E", "#FFFFFF", "川大"),
    ("nankai.png",     "#660066", "#FFFFFF", "南开"),
    ("tju.png",        "#003366", "#FFFFFF", "天大"),
    ("dlut.png",       "#003399", "#FFFFFF", "大连理工"),
    ("uestc.png",      "#003399", "#FFFFFF", "电子科大"),
    ("suda.png",       "#660066", "#FFFFFF", "苏大"),
    ("xmu.png",        "#1A3C6F", "#FFFFFF", "厦大"),
    ("hnu.png",        "#003399", "#FFFFFF", "湖大"),
    ("csu.png",        "#660066", "#FFFFFF", "中南"),
    # ---- 国际高校 ----
    ("stanford.png",   "#8C1515", "#FFFFFF", "S"),
    ("mit.png",        "#A31F34", "#FFFFFF", "MIT"),
    ("eth.png",        "#0066CC", "#FFFFFF", "ETH"),
    ("cambridge.png",  "#A3C1AD", "#000000", "Camb"),
    ("oxford.png",     "#002147", "#FFFFFF", "Oxf"),
    ("cmu.png",        "#C41230", "#FFFFFF", "CMU"),
    ("berkeley.png",   "#003262", "#FFFFFF", "Cal"),
    ("princeton.png",  "#E77500", "#FFFFFF", "Princ"),
    ("caltech.png",    "#FF6600", "#FFFFFF", "Caltech"),
    ("columbia.png",   "#003366", "#FFFFFF", "Columbia"),
    ("upenn.png",      "#0B3D91", "#FFFFFF", "UPenn"),
    ("nyu.png",        "#57068C", "#FFFFFF", "NYU"),
    ("usc.png",        "#990000", "#FFFFFF", "USC"),
    ("ucla.png",       "#2D6936", "#FFFFFF", "UCLA"),
    ("ucb.png",        "#003262", "#FFFFFF", "UCB"),
    ("uiuc.png",       "#1317CE", "#FFFFFF", "UIUC"),
    ("gatech.png",     "#A8340D", "#FFFFFF", "GT"),
    ("umich.png",      "#00274C", "#FFFFFF", "UMich"),
    ("uw.png",         "#4B2E83", "#FFFFFF", "UW"),
    ("ucsd.png",       "#006699", "#FFFFFF", "UCSD"),
    ("uci.png",        "#0066CC", "#FFFFFF", "UCI"),
    ("ucd.png",        "#003399", "#FFFFFF", "UCD"),
    ("ucsb.png",       "#003399", "#FFFFFF", "UCSB"),
    ("ucr.png",        "#003399", "#FFFFFF", "UCR"),
    ("ucsc.png",       "#003399", "#FFFFFF", "UCSC"),
    ("ucm.png",        "#003399", "#FFFFFF", "UCM"),
    # ---- 科技公司 ----
    ("tencent.png",    "#0052D9", "#FFFFFF", "T"),
    ("bytedance.png",  "#000000", "#FFFFFF", "字节"),
    ("alibaba.png",    "#FF6A00", "#FFFFFF", "A"),
    ("baidu.png",      "#2932E1", "#FFFFFF", "百度"),
    ("meituan.png",    "#FFCD00", "#000000", "美团"),
    ("huawei.png",     "#C7000B", "#FFFFFF", "华为"),
    ("xiaomi.png",     "#FF6900", "#FFFFFF", "MI"),
    ("didi.png",       "#FF6600", "#FFFFFF", "滴滴"),
    ("nvidia.png",     "#76B900", "#FFFFFF", "NV"),
    ("openai.png",     "#10A37F", "#FFFFFF", "AI"),
    ("google.png",     "#4285F4", "#FFFFFF", "G"),
    ("microsoft.png",  "#00A4EF", "#FFFFFF", "MS"),
    ("amazon.png",     "#FF9900", "#000000", "Amazon"),
    ("apple.png",      "#000000", "#FFFFFF", ""),
    ("meta.png",       "#0668E1", "#FFFFFF", "Meta"),
    ("anthropic.png",  "#D4A574", "#1A1A1A", "AN"),
    ("deepseek.png",   "#4A6CF7", "#FFFFFF", "DS"),
    ("moonshot.png",   "#6C5CE7", "#FFFFFF", "月"),
    ("minimax.png",    "#FF6B6B", "#FFFFFF", "MM"),
    ("alibaba-cloud.png", "#FF6A00", "#FFFFFF", "AC"),
    # ---- 其他 ----
    ("brand.png",      "#0B3D91", "#FFFFFF", "AD"),
]

SIZE = 256
RADIUS = 48


def _font_candidates():
    """Return font candidate paths based on OS."""
    system = _sys()
    if system == "Darwin":
        return [
            "/System/Library/Fonts/PingFang.ttc",
            "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
            "/System/Library/Fonts/Helvetica.ttc",
            "/Library/Fonts/Arial.ttf",
        ]
    elif system == "Linux":
        return [
            "/usr/share/fonts/truetype/noto/NotoSansCJK-Bold.ttc",
            "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        ]
    elif system == "Windows":
        windir = Path(os.environ.get("WINDIR", r"C:\Windows"))
        return [
            str(windir / "Fonts" / "msyh.ttc"),
            str(windir / "Fonts" / "msyhbd.ttc"),
            str(windir / "Fonts" / "arialbd.ttf"),
        ]
    return []


def find_font(size):
    """Cross-platform font finder with fallback."""
    for f in _font_candidates():
        if Path(f).exists():
            try:
                return ImageFont.truetype(f, size)
            except Exception:
                continue
    try:
        return ImageFont.load_default(size=size)
    except TypeError:
        return ImageFont.load_default()


def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def make_rounded_logo(bg, fg, label, size=SIZE):
    """Generate a rounded-corner placeholder logo as PIL Image."""
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    mask = Image.new("L", (size, size), 0)
    md = ImageDraw.Draw(mask)
    scale = size / 256
    md.rounded_rectangle((0, 0, size, size), radius=int(RADIUS * scale), fill=255)

    bg_layer = Image.new("RGBA", (size, size), hex_to_rgb(bg) + (255,))

    label = label or ""
    fs = int(140 * scale) if len(label) <= 1 else (int(110 * scale) if len(label) <= 2 else int(88 * scale))
    font = find_font(fs)

    draw = ImageDraw.Draw(bg_layer)
    if label:
        bbox = draw.textbbox((0, 0), label, font=font)
        tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
        ox = (size - tw) / 2 - bbox[0]
        oy = (size - th) / 2 - bbox[1]
        draw.text((ox, oy), label, fill=hex_to_rgb(fg), font=font)

    img.paste(bg_layer, (0, 0), mask)
    return img


def make_svg(bg, fg, label, size=SIZE):
    """Generate SVG string for a rounded-corner placeholder logo."""
    scale = size / 256
    r = int(RADIUS * scale)
    bg_r, bg_g, bg_b = hex_to_rgb(bg)
    fg_r, fg_g, fg_b = hex_to_rgb(fg)

    label = label or ""
    fs = int(140 * scale) if len(label) <= 1 else (int(110 * scale) if len(label) <= 2 else int(88 * scale))

    # Approximate text centering
    text_y = size / 2 + fs / 3

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 {size} {size}">
  <rect width="{size}" height="{size}" rx="{r}" ry="{r}" fill="rgb({bg_r},{bg_g},{bg_b})"/>
  <text x="50%" y="{text_y:.0f}" dominant-baseline="middle" text-anchor="middle"
        fill="rgb({fg_r},{fg_g},{fg_b})" font-size="{fs}" font-family="Arial, Helvetica, sans-serif" font-weight="bold">{label}</text>
</svg>'''
    return svg


def main():
    parser = argparse.ArgumentParser(description="Generate placeholder logos for resume-pro")
    parser.add_argument("--svg", action="store_true", help="Also generate SVG files")
    parser.add_argument("--only", choices=["png", "svg"], default=None,
                        help="Generate only the specified format (default: both if --svg)")
    parser.add_argument("--size", type=int, default=SIZE, help="Image size in pixels (default: 256)")
    parser.add_argument("--output", type=str, default=None, help="Output directory (default: script's directory)")
    args = parser.parse_args()

    out_dir = Path(args.output) if args.output else Path(__file__).parent
    out_dir.mkdir(parents=True, exist_ok=True)

    gen_png = args.only != "svg"
    gen_svg = args.only == "svg" or args.svg

    n = 0
    for filename, bg, fg, label in LOGOS:
        stem = Path(filename).stem
        img = make_rounded_logo(bg, fg, label, args.size)

        if gen_png:
            img.save(out_dir / filename, "PNG")
            n += 1

        if gen_svg:
            svg_content = make_svg(bg, fg, label, args.size)
            (out_dir / f"{stem}.svg").write_text(svg_content, encoding="utf-8")
            n += 1

    # Personal avatar: crop from ../hertz.jpg if exists
    src = Path(__file__).parent.parent.parent / "hertz.jpg"
    if src.exists():
        avatar = Image.open(src).convert("RGB")
        w, h = avatar.size
        s = min(w, h)
        avatar = avatar.crop(((w - s) // 2, (h - s) // 2, (w + s) // 2, (h + s) // 2))
        avatar = avatar.resize((args.size, args.size), Image.LANCZOS)
        avatar.save(out_dir / "avatar.png", "PNG")
        n += 1

    fmt = []
    if gen_png:
        fmt.append("PNG")
    if gen_svg:
        fmt.append("SVG")
    print(f"OK: {n} files ({'+'.join(fmt)}) written to {out_dir}")


if __name__ == "__main__":
    main()
