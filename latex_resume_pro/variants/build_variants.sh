#!/usr/bin/env bash
#
# build_variants.sh — 批量编译所有变体到 variants/pdf/
#
# 必须从 latex_resume_pro/ 目录运行（让相对路径 ../config.tex 等可解析）
#
# 用法：
#   bash variants/build_variants.sh          # 串行编译（默认）
#   bash variants/build_variants.sh -j 4    # 并行编译（4 个 job）
#

set -e
cd "$(dirname "$0")/.."

OUT="variants/pdf"
mkdir -p "$OUT"

VARIANTS=(
  "variants/variant-academic.tex"
  "variants/variant-academic-long.tex"
  "variants/variant-product.tex"
  "variants/variant-blackpro.tex"
  "variants/variant-minimalist.tex"
  "variants/variant-onepage.tex"
  "variants/variant-english.tex"
  "variants/variant-purple.tex"
  "variants/variant-twocolumn.tex"
  "variants/variant-coverletter.tex"
)

# 解析 -j 参数
JOBS=1
while [[ $# -gt 0 ]]; do
  case "$1" in
    -j) JOBS="${2:-$(nproc 2>/dev/null || sysctl -n hw.ncpu 2>/dev/null || echo 2)}"; shift 2 ;;
    *)  shift ;;
  esac
done

build_one() {
  local src="$1"
  local name
  name=$(basename "$src" .tex)
  echo "==> Building $name ..."
  xelatex -interaction=nonstopmode -halt-on-error -file-line-error \
    -output-directory="$OUT" -jobname="$name" "$src" > "$OUT/$name.compile.log" 2>&1 \
    && xelatex -interaction=nonstopmode -halt-on-error -file-line-error \
       -output-directory="$OUT" -jobname="$name" "$src" >> "$OUT/$name.compile.log" 2>&1
  echo "    ✓ $OUT/$name.pdf"
}

if [[ "$JOBS" -gt 1 ]]; then
  echo "=== Parallel build with $JOBS jobs ==="
  # 使用 xargs 实现并行
  printf '%s\n' "${VARIANTS[@]}" | xargs -P "$JOBS" -I {} bash -c 'build_one "$@"' _ {}
else
  for src in "${VARIANTS[@]}"; do
    build_one "$src"
  done
fi

# 清理中间文件
echo "==> Cleaning intermediate files ..."
( cd "$OUT" && rm -f *.aux *.log *.out *.toc *.synctex.gz *.fls *.fdb_latexmk *.xdv *.compile.log )

echo ""
echo "All variants built. PDFs in: $OUT/"
ls -la "$OUT"/*.pdf 2>/dev/null
