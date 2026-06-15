# .latexmkrc — latexmk 统一编译配置
# 用法：latexmk -xelatex resume-pro-zh.tex
#       或：make watch（已集成）

$pdf_mode = 0;           # 不用 pdflatex
$xelatex_mode = 1;       # 使用 xelatex
$xelatex = 'xelatex -synctex=1 -interaction=nonstopmode -file-line-error %O %S';

# 输出目录（保持默认，与 Makefile 一致）
$out_dir = '.';

# 清理规则
$clean_ext = 'synctex.gz synctex.gz(busy) run.xml tex.bak bbl bcf fdb_latexmk fls xdv';
