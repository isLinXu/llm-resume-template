<div align="center">

# LLM Resume Template

### 专业 LaTeX 简历模板

**像维护 LaTeX 论文一样维护你的简历** — 模块化 · 可主题化 · 可上传 Logo / 作品集 / 开源项目

专为 **AI / 算法 / 大模型 / 全栈** 等技术岗位优化，兼顾排版美感、内容密度与 ATS 友好

[![Build PDFs](https://github.com/isLinXu/llm-resume-template/actions/workflows/build.yml/badge.svg)](https://github.com/isLinXu/llm-resume-template/actions/workflows/build.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![XeLaTeX](https://img.shields.io/badge/Compiler-XeLaTeX-blue.svg)](https://www.overleaf.com/learn/XeLaTeX)

</div>

---

## ✨ 特性一览

| 维度 | 能力 |
|:---:|:---|
| 🎨 **主题色** | 内置 8 套 + 自定义主题（HEX 三色） |
| 🧩 **模块化** | 章节独立文件，像论文 `\input{Sec/...}` 一样组合 |
| ⚙️ **高度可配** | 个人信息、Logo、字体、间距、模式集中在 `config.tex` |
| 🖼️ **Logo 支持** | 教育 / 工作条目左侧支持机构 Logo，顶部支持头像 / 品牌 Logo（40+ 占位） |
| 📊 **技能可视化** | 进度条 / 五点等级 / 标签云 / GitHub 徽章 |
| 🗂️ **丰富条目** | 项目卡片 / 开源项目 / 作品集 / 论文 / 荣誉 / 时间线 |
| 🌍 **中英文** | `[zh]` / `[en]` class 选项一键切换 |
| 🖨️ **打印 / 紧凑** | `[monochrome]` 单色、`[compact]` 紧凑双模式 |
| 🔄 **10 套变体** | 学术 / 商务 / 极简 / 一页 / 产品 / 双栏 / 英文 / 紫色 / 求职信 / 学术长版 |
| 📱 **QR 码** | 页脚嵌入 QR 码，面试扫码直达个人主页 |
| 🛠️ **一键编译** | Makefile + latexmk + GitHub Actions CI |
| 🌐 **在线编辑器** | GitHub Pages 在线编辑 + PDF 预览 + 一键构建部署 |

---

## 🎨 主题色一览

| 主题 | 色块 | 主色 | 推荐场景 |
|:---|:---:|:---|:---|
| `techblue` | ![techblue](https://img.shields.io/badge/█-0B3D91-0B3D91) | `#0B3D91` | AI / 算法 / 后端（**默认**） |
| `businessblack` | ![businessblack](https://img.shields.io/badge/█-111827-111827) | `#111827` | 管理 / 咨询 / 金融 |
| `academicgray` | ![academicgray](https://img.shields.io/badge/█-1F2937-1F2937) | `#1F2937` | 科研 / 教职 / 申博 |
| `energyorange` | ![energyorange](https://img.shields.io/badge/█-C2410C-C2410C) | `#C2410C` | 产品 / 设计 / 创业 |
| `innovationgreen` | ![innovationgreen](https://img.shields.io/badge/█-065F46-065F46) | `#065F46` | 环保 / 生物 / 新能源 |
| `professionalpurple` | ![professionalpurple](https://img.shields.io/badge/█-5B21B6-5B21B6) | `#5B21B6` | 艺术 / 媒体 / 创意 |
| `crimson` | ![crimson](https://img.shields.io/badge/█-9F1239-9F1239) | `#9F1239` | 暗红 / 法律 / 文史 |
| `ocean` | ![ocean](https://img.shields.io/badge/█-0E7490-0E7490) | `#0E7490` | 海洋青 / 教育 |

> 💡 自定义主题：`\customtheme{0F172A}{2563EB}{E6EEFB}`（主色 / 次色 / 浅底 HEX）

---

## 🔄 变体速览

| 变体 | 主题 | 模式 | 适用场景 |
|:---|:---|:---|:---|
| `variant-academic` | 学术灰 | 默认 | 科研 / 申博 / 教职 |
| `variant-academic-long` | 学术灰 | 默认 | 教职 / 博后（3+ 页长版 CV） |
| `variant-blackpro` | 商务黑 | 默认 | 管理 / 咨询 / 金融 |
| `variant-product` | 活力橙 | compact | 产品 / 创业 / 设计 |
| `variant-minimalist` | 单色 | compact + mono | ATS / 黑白打印 |
| `variant-onepage` | 科技蓝 | compact + nofooter | 校招 / 应届一页 |
| `variant-english` | 科技蓝 | `[en]` | 海外申请 / 外企 |
| `variant-purple` | 专业紫 | 默认 | 艺术 / 媒体 / 创意 |
| `variant-twocolumn` | 海洋青 | nofooter | 双栏布局 / 快速浏览 |
| `variant-coverletter` | 科技蓝 | nofooter | 配套求职信 |

---

## 🚀 快速开始

### 1. 环境要求

- TeX Live ≥ 2020（推荐 2023+）
- 编译器：**XeLaTeX**
- Python 3.8+（仅用于 Logo 占位图生成）
- 字体（缺失会自动回退）：
  - 西文：IBM Plex Serif / Sans / Mono（回退 DejaVu / Liberation）
  - 中文：Noto Serif CJK SC / Noto Sans CJK SC（回退 PingFang SC / WenQuanYi / Source Han）

macOS 一键安装字体：

```bash
brew tap homebrew/cask-fonts
brew install --cask font-ibm-plex font-noto-serif-cjk-sc font-noto-sans-cjk-sc
```

### 2. 编译

```bash
cd latex_resume_pro

# 推荐：用 Makefile
make                # 构建主简历 → resume-pro-zh.pdf
make preview        # 主题预览 → themes-preview.pdf
make quickstart     # 极简示例 → quickstart.pdf
make variants       # 构建 9 套变体 → variants/pdf/
make all-pdf        # 一次性全部构建
make watch          # 文件变化自动重编译（依赖 latexmk）
make lint           # LaTeX 语法检查（chktex）

# 或直接 xelatex（跑两遍以稳定页码）
xelatex resume-pro-zh.tex
xelatex resume-pro-zh.tex
```

### 3. Docker 编译（无需本地安装 TeX Live）

```bash
docker build -t resume-builder .
docker run --rm -v $(pwd)/latex_resume_pro:/workspace resume-builder
```

### 4. GitHub Pages 在线编辑（推荐）

本项目自带 GitHub Pages 在线编辑器，无需本地安装任何环境：

1. **Fork 本仓库**到你的 GitHub 账号
2. 进入仓库 **Settings → Pages → Source** 选择 `GitHub Actions`
3. 访问 `https://你的用户名.github.io/llm-resume-template/` 即可使用在线编辑器
4. 在编辑器中修改内容 → 点击「🚀 构建PDF」→ CI 自动编译并部署 PDF

> 💡 在线编辑器功能一览：
>
> | 类别 | 功能 |
> |:---|:---|
> | **编辑模式** | 表单编辑器 + 代码编辑器双模式切换 |
> | **语法高亮** | LaTeX 语法高亮（命令/环境/注释/花括号分色） |
> | **变体切换** | 11 种变体一键切换（学术/商务/极简/一页/产品/双栏/英文/紫色/求职信/学术长版/快速入门） |
> | **主题配置** | 8 套主题色块预览 + 自定义三色 |
> | **可视化配置** | 语言/紧凑/单色/页脚开关 |
> | **模块管理** | 6 个模块独立开关切换 |
> | **个人信息** | 侧栏表单编辑姓名/联系方式/链接 |
> | **撤销/重做** | 50 步历史记录 |
> | **搜索/替换** | 正则搜索 + 单个/全部替换 |
> | **拖拽分割线** | 编辑区与预览区可拖拽调整比例 |
> | **自动保存** | 1.2s 防抖自动保存到 localStorage |
> | **快捷键** | Ctrl+S 保存 / Ctrl+1-7 切换模块 / Ctrl+Enter 构建 / ? 帮助 |
> | **GitHub API** | 一键提交修改并触发 CI 自动编译 |
> | **下载** | ZIP 打包下载 + PDF 直接下载 |
> | **PDF 预览** | 缩略图侧栏 / 适应宽度 / 全屏模式 / Ctrl+滚轮缩放 / 打印支持 |
> | **字符统计** | 实时字符数 + 行数显示 |

### 5. Overleaf 一键使用

[![Open in Overleaf](https://img.shields.io/badge/Open_in-Overleaf-46A1B8.svg)](https://overleaf.com/)

打包整个 `latex_resume_pro/` 目录上传到 Overleaf，编译器选择 **XeLaTeX** 即可。

---

## 🗂️ 项目结构

```
llm-resume-template/
├── README.md                    # 本文件
├── CONTRIBUTING.md             # 贡献指南
├── LICENSE                      # MIT 许可
├── CHANGELOG.md                 # 版本变更记录
├── Dockerfile                   # Docker 构建环境
├── docker-compose.yml           # Docker Compose 简化编译
├── .gitattributes              # Git 属性（二进制/换行符/语言检测）
├── .github/workflows/build.yml  # CI 自动构建 + PR 评论 + Release
├── .github/workflows/pages.yml  # GitHub Pages 部署 + PDF 编译
├── docs/                        # GitHub Pages 在线编辑器
│   ├── index.html              #   着陆页（特性展示 + 变体预览）
│   ├── editor.html             #   在线编辑器（表单+代码双模式）
│   └── preview.html            #   PDF 预览器（缩略图+全屏+缩放）
├── hertz.jpg                    # 头像源图
└── latex_resume_pro/            # 核心模板目录
    ├── resume-pro.cls           # 样式类（核心样式 / 命令 / 主题系统）v3.7
    ├── resume-pro-zh.tex        # 中文主文件（装配模块）
    ├── config.tex               # ⭐ 主要修改这个：个人信息 + 主题 + Logo + QR
    ├── quickstart.tex           # 极简单文件示例
    ├── themes-preview.tex       # 主题与组件视觉规范预览
    ├── .latexmkrc               # latexmk 编译配置
    ├── Makefile                 # 一键编译脚本
    ├── CHEATSHEET.md            # 命令速查表
    ├── README.md                # 详细使用文档
    ├── modules/                 # ⭐ 中文各章节，按需组合
    │   ├── header.tex           #   头部 + 摘要
    │   ├── skills.tex           #   专业技能
    │   ├── education.tex        #   教育背景
    │   ├── experience.tex       #   实习 / 工作 / 科研
    │   ├── projects.tex         #   项目 + 开源 + 作品集
    │   ├── publications.tex     #   论文 / 专利 / 荣誉
    │   └── summary.tex          #   自我评价 / 求职意向（可选）
    ├── modules-en/              # 英文版章节
    │   ├── header.tex
    │   ├── skills.tex
    │   ├── education.tex
    │   ├── experience.tex
    │   ├── projects.tex
    │   ├── publications.tex
    │   └── summary.tex           #   Self-assessment & career objective
    ├── variants/                # 10 套场景变体
    │   ├── variant-academic.tex #   学术灰 / 申博 / 教职
    │   ├── variant-academic-long.tex # 长版学术 CV（3+ 页）
    │   ├── variant-blackpro.tex #   商务黑 / 管理 / 金融
    │   ├── variant-product.tex  #   活力橙 / 产品 / 创业
    │   ├── variant-minimalist.tex # 极简 / ATS / 黑白打印
    │   ├── variant-onepage.tex  #   极简一页 / 校招 / 应届
    │   ├── variant-english.tex  #   英文版 / 海外申请
    │   ├── variant-purple.tex  #   专业紫 / 创意 / 媒体
    │   ├── variant-twocolumn.tex # 双栏布局 / 快速浏览
    │   ├── variant-coverletter.tex # 求职信
    │   ├── build_variants.sh    #   批量编译脚本（支持 -j 并行）
    │   └── pdf/                 #   编译产物（gitignore）
    └── logos/                   # 机构 Logo（50+ 占位 + 自动生成）
        ├── build_placeholders.py #  Logo 占位图生成脚本（PNG + SVG）
        └── *.png                #   占位 / 真实 Logo
```

---

## 📚 命令速查

| 命令 | 说明 |
|:---|:---|
| `\name{...}` / `\tagline{...}` / `\keywords{...}` | 基本身份 |
| `\phone` / `\email` / `\github` / `\linkedin` / `\website` / `\blog` / `\location` / `\wechat` / `\zhihu` / `\scholar` / `\orcid` / `\homepage` | 联系方式 |
| `\photo{<file>}` / `\headerlogo{<file>}` | 头部右侧图像 |
| `\qrlink{<url>}` | 页脚 QR 码（可选） |
| `\setMaxPages{N}` | 页数限制（超出警告） |
| `\sectionTitle{<标题>}{<faIcon>}` | 章节标题（带图标 + 细线） |
| `\educationItem[<logo>]{校名}{时间}{专业}{学位}` | 教育条目 |
| `\experienceItem[<logo>]{公司}{时间}{职位}{itemize}` | 工作 / 实习 / 科研 |
| `\projectCard{标题}{时间}{一句话}{itemize}{链接}` | 卡片化项目 |
| `\openSourceItem{repo}{stars}{forks}{语言}{描述}{itemize}` | 开源贡献 |
| `\workItem[<thumb>]{标题}{平台}{链接}{描述}` | 作品集 |
| `\publicationItem{标题}{作者}{venue}{links}` | 论文 |
| `\awardItem{名称}{时间}{说明}` | 荣誉 / 专利 / 竞赛 |
| `\skillbar{技能}{0-10}` / `\skilldots{技能}{1-5}` | 技能可视化 |
| `\skilltag{文本}` / `\skilltagAccent{文本}` | 技能标签 |
| `\badge{左}{右}` | GitHub 风格双段徽章 |
| `\timelineEntry{日期}{标题}{描述}{内容}` | 时间线条目 |
| `\coverletterheader{姓名}{职位}{公司}{地址}` | 求职信信封头 |
| `\certItem{证书名}{颁发机构}{时间}` | 证书条目 |
| `\resumeItem{标题}{时间}{描述}` | 通用简历条目 |
| `\hdiv` | 主题色分割线 |
| `\hltext{文本}` | 高亮标签 |
| `\daterange{起}{止}` | 日期范围快捷 |
| `\rpIfPageOne{内容}` | 仅首页渲染 |
| `\conditionalSection[show\|hide\|compact-only]{标题}{图标}{内容}` | 条件章节 |
| `\lastupdated` | 自动中英文「最后更新」日期 |
| `\watermark{文本}` | 水印（如 DRAFT） |

> 完整原语 + 视觉效果可编译 `themes-preview.tex` 查看，或参阅 `CHEATSHEET.md`。

---

## 🎯 内容写作最佳实践

### 通用准则

- **量化优先**：每条要点尽量带数字（`+15%`、`P99 1.8s`、`5B tokens`、`Top 1%`）
- **STAR 表达**：背景 → 任务 → 行动 → 结果（结果要可验证）
- **关键词命中**：在「技能」「项目」中重复 JD 关键词，提高 ATS 匹配
- **页数控制**：应届 1 页、3 年内 1-2 页、5 年以上最多 2 页（用 `[compact]` 进一步压紧）

### 技术岗加分项

- 用 `\projectCard` 把一个旗舰项目讲透：技术栈 / 核心方案 / 消融实验 / 业务效果
- 用 `\openSourceItem` 展示 GitHub 数字（Stars / Forks / Language）
- 用 `\publicationItem` 标注 venue 等级（CCF-A / CCF-B / arXiv）
- 用 `\workItem` 展示博客 / 视频 / 知乎专栏 / 技术分享
- 用 `\qrlink{...}` 让面试官扫码直达你的作品集

---

## 🔧 常见问题

<details>
<summary><b>Q1：编译报错 <code>Font shape ... undefined</code>?</b></summary>

缺失 IBM Plex / Noto CJK 字体。模板内置回退（PingFang SC），但建议安装齐全字体。Linux 用户可安装 `fonts-noto-cjk` 包。

</details>

<details>
<summary><b>Q2：Logo 不显示？</b></summary>

① 检查路径是否相对 `latex_resume_pro/`；② 确认在 `config.tex` 里 `\def\xxxLogo{...}` 路径非空；③ 模块中用 `[\xxxLogo]` 而不是 `[xxxLogo]`。

</details>

<details>
<summary><b>Q3：想改字体？</b></summary>

在 `resume-pro.cls` 里搜索 `\setmainfont` 一段，按需替换为本地字体名。

</details>

<details>
<summary><b>Q4：如何只导出黑白版本？</b></summary>

`\documentclass[zh, monochrome]{resume-pro}` 即可。

</details>

<details>
<summary><b>Q5：英文简历？</b></summary>

复制 `resume-pro-zh.tex` 为 `resume-pro-en.tex`，class 改为 `[en]`，模块改成英文文本。或直接使用 `variants/variant-english.tex`。

</details>

<details>
<summary><b>Q6：怎么调整章节顺序 / 隐藏章节？</b></summary>

直接编辑主文件中的 `\input{...}` 行（注释 `%` 即可隐藏）。

</details>

<details>
<summary><b>Q7：内容太多溢出到第 N 页怎么办？</b></summary>

① 加 `[compact]` 选项；② 删除次要要点（每条经历控制在 3-5 条）；③ 隐藏 `summary.tex`；④ 使用 `\setMaxPages{1}` 获得溢出警告。

</details>

<details>
<summary><b>Q8：QR 码怎么用？</b></summary>

在 `config.tex` 中取消注释 `\qrlink{https://your-url}`，页脚右侧会出现小 QR 码。

</details>

<details>
<summary><b>Q9：Linux 下中文字体怎么安装？</b></summary>

```bash
# Ubuntu / Debian
sudo apt install fonts-noto-cjk fonts-ibm-plex

# Fedora
sudo dnf install google-noto-sans-cjk-sc-fonts google-noto-serif-cjk-sc-fonts
```

</details>

<details>
<summary><b>Q10：如何调试排版溢出？</b></summary>

使用 `[debug]` 选项编译，会显示文本边界框和溢出标记：

```latex
\documentclass[zh,debug]{resume-pro}
```

终端中也会输出 `\overfullrule` 标记的溢出位置。

</details>

---

## 📜 许可

MIT License — 可自由使用、修改、分发。详见 [LICENSE](LICENSE)。

## 🤝 贡献

欢迎提交 Issue / PR 改进模板。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

建议方向：

- 新主题色（提供 `\customtheme{...}` 参数即可）
- 新模块（在 `modules/` 加新文件）
- 字体回退优化（Linux / Windows 默认中文字体兼容）
- 新变体（在 `variants/` 加新文件）

---

**Have fun crafting your resume! 🎉**
