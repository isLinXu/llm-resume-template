# ============================================================
# Dockerfile — 可复现的 LaTeX 简历构建环境
# ------------------------------------------------------------
# 用法：
#   docker build -t resume-builder .
#   docker run --rm -v $(pwd)/latex_resume_pro:/workspace resume-builder
#
# 自定义编译目标：
#   docker run --rm -v $(pwd)/latex_resume_pro:/workspace \
#     resume-builder xelatex resume-pro-zh.tex
#
# 使用 docker compose：
#   docker compose up
# ============================================================

FROM danteev/texlive:latest

# 安装 Python（Logo 生成脚本依赖 Pillow）
RUN apt-get update && \
    apt-get install -y --no-install-recommends python3 python3-pip && \
    pip3 install --no-cache-dir Pillow && \
    rm -rf /var/lib/apt/lists/*

# 安装中文字体（Noto CJK）+ IBM Plex（西文首选字体）
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      fonts-noto-cjk \
      fonts-noto-cjk-extra \
      fonts-ibm-plex \
    && rm -rf /var/lib/apt/lists/*

# 设置工作目录
WORKDIR /workspace

# 默认编译主简历（跑两遍稳定页码）
CMD ["sh", "-c", "xelatex -interaction=nonstopmode resume-pro-zh.tex && xelatex -interaction=nonstopmode resume-pro-zh.tex"]
