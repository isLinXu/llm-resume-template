#!/usr/bin/env bash
# Docker 编译验证脚本 — 编译所有 12 个 PDF
set -e
cd "$(dirname "$0")"

IMG="resume-builder-test"
echo "=== Building Docker image ==="
docker build -t "$IMG" ../../ 2>&1 | tail -3

echo ""
echo "=== Compiling main resume ==="
docker run --rm -v "$(pwd):/workspace" "$IMG" sh -c "cd /workspace && xelatex -interaction=nonstopmode resume-pro-zh.tex && xelatex -interaction=nonstopmode resume-pro-zh.tex" 2>&1 | grep "Output written"

echo ""
echo "=== Compiling quickstart ==="
docker run --rm -v "$(pwd):/workspace" "$IMG" sh -c "cd /workspace && xelatex -interaction=nonstopmode quickstart.tex && xelatex -interaction=nonstopmode quickstart.tex" 2>&1 | grep "Output written"

echo ""
echo "=== Compiling themes-preview ==="
docker run --rm -v "$(pwd):/workspace" "$IMG" sh -c "cd /workspace && xelatex -interaction=nonstopmode themes-preview.tex && xelatex -interaction=nonstopmode themes-preview.tex" 2>&1 | grep "Output written"

echo ""
echo "=== Compiling all variants ==="
for v in variant-academic variant-academic-long variant-blackpro variant-product variant-minimalist variant-onepage variant-english variant-purple variant-twocolumn variant-coverletter; do
  echo "--- $v ---"
  docker run --rm -v "$(pwd):/workspace" "$IMG" sh -c "cd /workspace && xelatex -interaction=nonstopmode -halt-on-error -output-directory=variants/pdf -jobname=$v variants/${v}.tex && xelatex -interaction=nonstopmode -halt-on-error -output-directory=variants/pdf -jobname=$v variants/${v}.tex" 2>&1 | grep "Output written"
done

echo ""
echo "=== All 12 PDFs compiled successfully! ==="
