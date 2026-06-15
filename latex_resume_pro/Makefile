## ============================================================
##  Makefile — resume-pro 编译脚本
##  -----------------------------------------------------------
##    make            构建主简历 PDF（默认 resume-pro-zh）
##    make quick      只编译一次（草稿快速预览）
##    make watch      文件变化自动重新编译（依赖 latexmk）
##    make preview    构建主题预览 PDF
##    make quickstart 构建极简示例 PDF
##    make variants   构建全部 variants 到 variants/pdf/
##    make logos      重新生成占位 Logo + 头像
##    make all-pdf    一次性构建所有 PDF（主 + 预览 + quickstart + variants）
##    make lint       检查 LaTeX 语法（chktex）
##    make clean      清理中间文件
##    make distclean  清理中间文件 + PDF
## ============================================================

MAIN       = resume-pro-zh
PREVIEW    = themes-preview
QUICKSTART = quickstart

LATEX      = xelatex
LATEX_FLAGS = -interaction=nonstopmode -halt-on-error -file-line-error

# 并行编译 job 数（用于 variants 批量构建）
JOBS       ?= 2

.PHONY: all default quick latexmk watch preview quickstart variants logos \
        all-pdf lint clean distclean help

default: all

all: $(MAIN).pdf

%.pdf: %.tex
	$(LATEX) $(LATEX_FLAGS) $<
	$(LATEX) $(LATEX_FLAGS) $<

quick:
	$(LATEX) $(LATEX_FLAGS) $(MAIN).tex

latexmk:
	latexmk -xelatex -interaction=nonstopmode $(MAIN).tex

watch:
	latexmk -xelatex -pvc -interaction=nonstopmode $(MAIN).tex

preview: $(PREVIEW).pdf

quickstart: $(QUICKSTART).pdf

variants:
	@bash variants/build_variants.sh -j $(JOBS)

logos:
	@cd logos && python3 build_placeholders.py

logos-svg:
	@cd logos && python3 build_placeholders.py --svg

all-pdf: $(MAIN).pdf $(PREVIEW).pdf $(QUICKSTART).pdf variants
	@echo "=== Building all PDFs ==="
	@for v in variants/variant-*.tex; do \
		if [ -f "$v" ]; then \
			xelatex -interaction=nonstopmode -halt-on-error "$v"; \
		fi; \
	done
	@echo "=== Done ==="

## ---------- Lint ----------
lint:
	@echo "=== Checking LaTeX files with chktex ==="
	@find . -name '*.tex' -not -path './variants/pdf/*' | while read f; do \
		chktex -q -n2 -n24 -n13 "$f" 2>/dev/null || true; \
	done
	@echo "=== Done ==="

## ---------- Clean ----------
clean:
	rm -f *.aux *.log *.out *.toc *.synctex.gz *.fls *.fdb_latexmk *.xdv *.bbl *.blg
	rm -f variants/pdf/*.aux variants/pdf/*.log variants/pdf/*.out variants/pdf/*.toc variants/pdf/*.compile.log

distclean: clean
	rm -f $(MAIN).pdf $(PREVIEW).pdf $(QUICKSTART).pdf
	rm -f variants/pdf/*.pdf

help:
	@echo "make            构建主简历 PDF ($(MAIN).pdf)"
	@echo "make preview    构建主题预览 PDF"
	@echo "make quickstart 构建极简示例 PDF"
	@echo "make variants   构建 variants 到 variants/pdf/（支持 -j 并行）"
	@echo "make logos      重新生成占位 Logo (PNG)"
	@echo "make logos-svg  重新生成占位 Logo (PNG + SVG)"
	@echo "make all-pdf    构建所有 PDF（含 variants）"
	@echo "make watch      文件变化自动重编译"
	@echo "make lint       LaTeX 语法检查（chktex）"
	@echo "make clean      清理中间文件"
	@echo "make distclean  清理中间文件 + PDF"

## ---------- GitHub Actions ----------
##
## 添加 lint 步骤到 CI 流水线
## 添加 logos-svg 步骤到 CI 流水线
## 添加 all-pdf 步骤到 CI 流水线
## 在 PR 评论中显示构建结果
## 自动创建 Tag Release
