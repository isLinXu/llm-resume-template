# resume-pro · 9 套变体（variants）

> 通过对 `resume-pro.cls` 的不同主题 / 形状 / 模式 / 章节顺序组合，生成针对不同岗位场景的简历变体。
> 所有变体共享 `../config.tex` 与 `../modules/*.tex`，**只覆写主题、形状、章节顺序**。

## 变体一览

| 变体文件 | 主题 | 头像形状 | Class 选项 | 章节顺序特点 | 适用场景 |
|---|---|---|---|---|---|
| `variant-academic.tex` | academicgray | rounded | (default) | 论文先于项目 | 科研 / 申博 / 教职 |
| `variant-academic-long.tex` | academicgray | rounded | (default) | 研究兴趣+学术服务+教学+交流 | 教职 / 博后 / 长版学术 CV |
| `variant-product.tex` | energyorange | circular | `compact` | 经历先于教育 | 产品 / 创业 / 设计 |
| `variant-blackpro.tex` | businessblack | square | (default) | 经历最前 | 管理 / 咨询 / 金融 |
| `variant-minimalist.tex` | (mono) | (无) | `compact + monochrome` | 略去 projects | ATS / 黑白打印 |
| `variant-onepage.tex` | techblue | circular | `compact + nofooter` | 精选核心+代表成果 | 校招 / 应届一页 |
| `variant-english.tex` | techblue | circular | `en` | 全英文 | 海外申请 / 外企 |
| `variant-purple.tex` | professionalpurple | square | (default) | 项目/作品集最前 | 艺术 / 媒体 / 创意 |
| `variant-twocolumn.tex` | ocean | circular | `nofooter` | 双栏 sidebar | 快速浏览 / 求职平台 |
| `variant-coverletter.tex` | techblue | — | `nofooter` | 求职信三段式 | 配套求职信 |

## 一键编译

从 `latex_resume_pro/` 目录：

```bash
make variants                 # 推荐
# 或
bash variants/build_variants.sh
```

产物输出到 `variants/pdf/`：

```
variants/pdf/
├── variant-academic.pdf
├── variant-academic-long.pdf
├── variant-blackpro.pdf
├── variant-english.pdf
├── variant-minimalist.pdf
├── variant-onepage.pdf
├── variant-product.pdf
├── variant-purple.pdf
├── variant-twocolumn.pdf
└── variant-coverletter.pdf
```

## 创建你自己的变体

复制任一 `variant-*.tex`，按需调整：

```latex
\documentclass[zh]{resume-pro}    % 或 [zh,compact] / [zh,monochrome] 等
\input{config.tex}                 % 复用全局配置

\settheme{techblue}                % 主题（覆盖 config）
\photoshape{circular}              % 头像形状
\version{MyVariant \textbullet\ \today}

\begin{document}
\input{modules/header.tex}
\input{modules/skills.tex}
\input{modules/education.tex}
\input{modules/experience.tex}
% 按需插入 / 注释 / 重排
\end{document}
```

把新文件加入 `build_variants.sh` 的 `VARIANTS=(...)` 数组即可参与批量编译。

## 创建独立内容的变体

如果你想要某个变体使用**完全不同的内容**（例如英文版），只需：

1. 复制 `modules/` 为 `modules-xxx/` 并改写
2. 在变体主文件中 `\input{modules-xxx/header.tex}` 等
3. 不再 `\input{config.tex}`，改在主文件直接写 `\name{...}` 等

参考 `variant-english.tex` 配合 `modules-en/` 的做法。
