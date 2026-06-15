#!/bin/sh
# Docker entrypoint for building a single variant
cd /workspace
VARIANT="$1"
if [ -z "$VARIANT" ]; then
  # Default: build main resume
  xelatex -interaction=nonstopmode resume-pro-zh.tex
  xelatex -interaction=nonstopmode resume-pro-zh.tex
else
  xelatex -interaction=nonstopmode -halt-on-error -output-directory=variants/pdf -jobname="$VARIANT" "variants/${VARIANT}.tex"
  xelatex -interaction=nonstopmode -halt-on-error -output-directory=variants/pdf -jobname="$VARIANT" "variants/${VARIANT}.tex"
fi
