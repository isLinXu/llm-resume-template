# resume-pro · 专业 LaTeX 简历模板（v3.9.0）

> 像维护 LaTeX 论文一样维护你的简历 — 模块化、可主题化、可上传 Logo / 作品集 / 开源项目。
> 专为 **AI / 算法 / 大模型 / 全栈** 等技术岗位优化，兼顾排版美感、内容密度与 ATS 友好。

---

## ✨ 特性一览

| 维度 | 能力 |
|---|---|
| 🎨 主题色 | 内置 8 套（科技蓝 / 商务黑 / 学术灰 / 活力橙 / 创新绿 / 专业紫 / 暗红 / 海洋青）+ 自定义主题 |
| 🧩 模块化 | 章节单独存放在 `modules/`，像论文 `\input{Sec/...}` 一样组合 |
| ⚙️ 高度可配 | 个人信息、Logo、字体、间距、模式都集中在 `config.tex` |
| 🖼️ Logo 支持 | 教育 / 工作条目左侧支持机构 Logo，顶部右侧支持个人品牌 Logo / 圆形头像 |
| 📊 技能可视化 | 进度条 (`\skillbar`) / 五点等级 (`\skilldots`) / 标签云 (`\skilltag`) / 徽章 (`\badge`) |
| 🗂️ 项目卡片 | `\projectCard` 项目 / `\openSourceItem` 开源 / `\workItem` 作品集 / `\publicationItem` 论文 / `\awardItem` 荣誉 |
| 🌍 中英文 | `[zh]` / `[en]` class 选项一键切换 |
| 🖨️ 打印 / 紧凑 | `[monochrome]` 单色、`[compact]` 紧凑双模式 |
| 🛠️ 一键编译 | Makefile 提供 `make` / `make watch` / `make all-pdf` |

---

## 🚀 快速开始

### 1. 环境要求

- TeX Live ≥ 2020（推荐 2023+）
- 编译器：**XeLaTeX**
- 字体（任一组合可用即可，缺失会自动回退）：
  - 西文：IBM Plex Serif / Sans / Mono
  - 中文：Noto Serif CJK SC / Noto Sans CJK SC（或回退到 PingFang SC）

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
make all-pdf        # 一次性全部构建
make watch          # 文件变化自动重编译（依赖 latexmk）

# 或直接 xelatex（跑两遍以稳定页码）
xelatex resume-pro-zh.tex
xelatex resume-pro-zh.tex
```

### 3. Overleaf 一键使用

打包整个 `latex_resume_pro/` 目录上传到 Overleaf，编译器选择 **XeLaTeX** 即可。

---

## 🗂️ 项目结构

```
latex_resume_pro/
├── resume-pro.cls          # 样式类（核心样式 / 命令 / 主题系统）
├── resume-pro-zh.tex       # 中文主文件（装配模块）
├── config.tex              # ⭐ 主要修改这个：个人信息 + 主题 + Logo
├── quickstart.tex          # 极简单文件示例（适合学命令）
├── themes-preview.tex      # 主题与组件视觉规范预览
├── Makefile                # 一键编译脚本
├── README.md               # 本文档
├── modules/                # ⭐ 各章节，按需组合
│   ├── header.tex          # 头部 + 摘要
│   ├── skills.tex          # 专业技能
│   ├── education.tex       # 教育背景
│   ├── experience.tex      # 实习 / 工作 / 科研
│   ├── projects.tex        # 项目 + 开源 + 作品集
│   ├── publications.tex    # 论文 / 专利 / 荣誉
│   └── summary.tex         # 自我评价 / 求职意向（可选）
└── logos/                  # 机构 Logo（PNG/JPG/PDF）
```

---

## 🎨 主题系统

### 内置主题

| 命令 | 主色 | 推荐场景 |
|---|---|---|
| `\settheme{techblue}` | `#0B3D91` | AI / 算法 / 后端（默认） |
| `\settheme{businessblack}` | `#111827` | 管理 / 咨询 / 金融 |
| `\settheme{academicgray}` | `#1F2937` | 科研 / 教职 / 申博 |
| `\settheme{energyorange}` | `#C2410C` | 产品 / 设计 / 创业 |
| `\settheme{innovationgreen}` | `#065F46` | 环保 / 生物 / 新能源 |
| `\settheme{professionalpurple}` | `#5B21B6` | 艺术 / 媒体 / 创意 |
| `\settheme{crimson}` | `#9F1239` | 暗红 / 法律 / 文史 |
| `\settheme{ocean}` | `#0E7490` | 海洋青 / 教育 |

### 自定义主题

```latex
% \customtheme{<主色HEX>}{<次色HEX>}{<浅底HEX>}
\customtheme{0F172A}{2563EB}{E6EEFB}
```

### Class 选项

```latex
\documentclass[zh]{resume-pro}              % 中文（默认）
\documentclass[en]{resume-pro}              % 英文
\documentclass[zh, monochrome]{resume-pro}  % 单色（适合打印）
\documentclass[zh, compact]{resume-pro}     % 紧凑模式
```

---

## 🖼️ Logo 与照片

### 头部右侧（个人头像 / 品牌 Logo）

`config.tex` 中二选一：

```latex
\photo{hertz.jpg}              % 圆形头像
% 或
\headerlogo{logos/brand.png}        % 矩形品牌 Logo
```

### 教育 / 工作条目左侧 Logo

1. 把 PNG 放进 `logos/`，例如 `logos/tsinghua.png`
2. 在 `config.tex` 注册短宏：

   ```latex
   \def\tsinghuaLogo{logos/tsinghua.png}
   \def\tencentLogo{logos/tencent.png}
   ```

3. 在模块中使用：

   ```latex
   \educationItem[\tsinghuaLogo]{清华大学}{2023.09 -- 2026.06}{计算机科学与技术}{硕士}
   \experienceItem[\tencentLogo]{腾讯 AI Lab}{2023.06 -- 2024.03}{算法实习生}{...}
   ```

> **未提供 Logo 时**：左侧自动渲染默认图标（教育 → `\faUniversity`，工作 → `\faBuilding`）。

---

## 📚 命令速查表

| 命令 | 说明 |
|---|---|
| `\name{<姓名>}` / `\tagline{<标语>}` / `\keywords{...}` | 基本身份 |
| `\phone` / `\email` / `\github` / `\linkedin` / `\website` / `\blog` / `\location` / `\birthday` / `\wechat` / `\zhihu` / `\scholar` / `\orcid` | 联系方式（任意可省） |
| `\photo{<file>}` / `\headerlogo{<file>}` | 头部右侧图像 |
| `\sectionTitle{<标题>}{<faIcon>}` | 章节标题（带图标 + 竖条 + 下划线） |
| `\educationItem[<logo>]{校名}{时间}{专业}{学位/附注}` | 教育条目 |
| `\experienceItem[<logo>]{公司}{时间}{职位}{itemize 内容}` | 工作 / 实习 / 科研 |
| `\projectCard{标题}{时间}{一句话}{itemize 详细}{链接 footer}` | 卡片化项目 |
| `\openSourceItem{repo}{stars}{forks}{语言}{描述}{itemize}` | 开源贡献 |
| `\workItem[<thumb>]{标题}{平台}{链接}{描述}` | 作品集（博客 / 视频 / 设计） |
| `\publicationItem{标题}{作者}{venue}{links}` | 论文 |
| `\awardItem{名称}{时间}{说明}` | 荣誉 / 专利 / 竞赛 |
| `\skillbar{技能}{0-10}` | 横向进度条 |
| `\skilldots{技能}{1-5}` | 五点等级 |
| `\skilltag{文本}` / `\skilltagAccent{文本}` | 技能标签（描边 / 实底） |
| `\badge{左}{右}` | GitHub 风格双段徽章 |
| `\timelineEntry{日期}{标题}{描述}` | 时间线条目 |

> 完整原语 + 视觉效果可编译 `themes-preview.tex` 查看。

---

## 🧪 像论文一样修改

整个模板设计参照学术论文工程化经验：

- **「装配文件」+「章节文件」分离** — `resume-pro-zh.tex` 只负责 `\input{modules/...}`，所有内容写在 `modules/` 下
- **集中配置** — `config.tex` 是唯一全局可调点，主题、姓名、联系方式、Logo 路径都在这里
- **稳定语义命令** — 命令名（`\projectCard` / `\experienceItem`）按内容语义命名，不与样式细节耦合
- **可重排** — 在主文件里调换 `\input` 顺序即可调换章节顺序，注释掉某行即可隐藏整章

例如想把「项目」放到「教育」之前：

```latex
\input{modules/header.tex}
\input{modules/skills.tex}
\input{modules/projects.tex}    % ← 上移
\input{modules/education.tex}
\input{modules/experience.tex}
\input{modules/publications.tex}
% \input{modules/summary.tex}   % ← 注释即可隐藏
```

新增自定义章节：

1. 新建 `modules/volunteer.tex`，里面用现成原语写内容
2. 在主文件加一行 `\input{modules/volunteer.tex}` 即可

---

## 🎯 内容写作最佳实践

### 1. 通用准则

- **量化优先**：每条要点尽量带数字（`+15%`、`P99 1.8s`、`5B tokens`、`Top 1%`）
- **STAR 表达**：背景 → 任务 → 行动 → 结果（结果要可验证）
- **关键词命中**：在「技能」「项目」中重复 JD 关键词，提高 ATS 匹配
- **页数控制**：应届 1 页、3 年内 1-2 页、5 年以上最多 2 页（用 `[compact]` 进一步压紧）

### 2. 技术岗加分项（强烈推荐）

- 用 `\projectCard` 把一个旗舰项目讲透：技术栈 / 核心方案 / 消融实验 / 业务效果
- 用 `\openSourceItem` 展示 GitHub 数字（Stars / Forks / Language）
- 用 `\publicationItem` 标注 venue 等级（CCF-A / CCF-B / arXiv）
- 用 `\workItem` 展示博客 / 视频 / 知乎专栏 / 技术分享，体现技术品牌力

### 3. ATS 友好

- 章节标题用标准词：`教育背景` / `工作经历` / `项目经历`（已在模板中）
- 不要把关键信息嵌入图片
- 字体优先 PDF 内嵌可复制粘贴的（XeLaTeX + 标准字体均满足）

---

## 🔧 常见问题（FAQ）

**Q1：编译报错 `Font shape ... undefined`?**
A：缺失 IBM Plex / Noto CJK 字体。模板内置回退（PingFang SC），但建议安装齐全字体。

**Q2：Logo 不显示？**
A：① 检查路径是否相对 `latex_resume_pro/`；② 确认在 `config.tex` 里 `\def\xxxLogo{...}` 路径非空；③ 模块中用 `[\xxxLogo]` 而不是 `[xxxLogo]`。

**Q3：想改字体？**
A：在 `resume-pro.cls` 里搜索 `\setmainfont` 一段，按需替换为本地字体名。

**Q4：如何只导出黑白版本？**
A：`\documentclass[zh, monochrome]{resume-pro}` 即可。

**Q5：英文简历？**
A：复制 `resume-pro-zh.tex` 为 `resume-pro-en.tex`，class 改为 `[en]`，模块改成英文文本。

**Q6：怎么调整章节顺序 / 隐藏章节？**
A：直接编辑主文件 `resume-pro-zh.tex` 中的 `\input{...}` 行（注释 `%` 即可隐藏）。

**Q7：内容太多溢出到第 N 页怎么办？**
A：① 加 `[compact]` 选项；② 删除次要要点（每条经历控制在 3-5 条）；③ 隐藏 `summary.tex`。

---

## 📜 许可

MIT License — 可自由使用、修改、分发。

## 🤝 贡献

欢迎提交 Issue / PR 改进模板。建议方向：

- 新主题色（提供 `\customtheme{...}` 参数即可）
- 新模块（在 `modules/` 加新文件）
- 字体回退优化（Linux / Windows 默认中文字体兼容）

---

## 📂 三个示例文件用途

| 文件 | 用途 | 编译产物 |
|---|---|---|
| `resume-pro-zh.tex` | **正式简历主文件**（你最终交付的简历） | `resume-pro-zh.pdf` |
| `quickstart.tex` | 单文件极简示例，5 分钟入门所有命令 | `quickstart.pdf` |
| `themes-preview.tex` | 视觉规范预览，看当前主题下所有组件长什么样 | `themes-preview.pdf` |

---

**Have fun crafting your resume! 🎉**
