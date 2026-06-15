# resume-pro 命令速查表

> 所有命令都在 `resume-pro.cls` 中定义。本文件按使用频率分组，方便随时翻阅。

---

## 1. 个人信息（写在 `config.tex`）

```latex
\name{Hertz}
\tagline{大模型算法工程师 | 模型压缩 | 多模态}
\keywords{LLM · PyTorch · DeepSpeed · RAG · Agent}

\phone{+86 138-0000-0000}
\email{adong@example.com}
\github{hertz}              % 仅用户名，自动拼 https://github.com/...
\linkedin{hertz}            % 仅用户名，自动拼 https://linkedin.com/in/...
\website{https://hertz.dev}   % 完整 URL
\blog{https://blog.hertz.dev}
\location{北京·海淀}
\birthday{2000-01}
\wechat{hertz}
\zhihu{hertz}
\scholar{https://scholar.google.com/...}
\orcid{0000-0000-0000-0000}
\homepage{https://hertz.dev}  % 个人主页（出现在联系方式行）

\photo{hertz.jpg}           % 圆形头像
% \headerlogo{logos/brand.png}   % 二选一

% 页脚 QR 码（可选，指向个人主页 / GitHub / 作品集）
% \qrlink{https://hertz.dev}

% 页数限制（可选，超出时终端警告）
% \setMaxPages{1}
```

---

## 2. 主题与模式

```latex
% Class 选项
\documentclass[zh]{resume-pro}              % 中文
\documentclass[en]{resume-pro}              % 英文
\documentclass[zh, compact]{resume-pro}     % 紧凑
\documentclass[zh, monochrome]{resume-pro}  % 单色（打印）

% 主题
\settheme{techblue}        % 内置：techblue / businessblack / academicgray
                           %       energyorange / innovationgreen / professionalpurple
                           %       crimson / ocean
\customtheme{0F172A}{2563EB}{E6EEFB}   % 自定义（主色/次色/浅底，HEX）
```

---

## 3. 章节标题

```latex
\sectionTitle{专业技能}{\faLaptopCode}
\sectionTitle{教育背景}{\faGraduationCap}
\sectionTitle{实习经历}{\faBriefcase}
\sectionTitle{科研经历}{\faFlask}
\sectionTitle{项目经历}{\faProjectDiagram}
\sectionTitle{开源贡献}{\faGithub}
\sectionTitle{作品集}{\faPalette}
\sectionTitle{论文与专利}{\faFile*}
\sectionTitle{荣誉与竞赛}{\faTrophy}
\sectionTitle{自我评价}{\faUserCheck}
\sectionTitle{求职意向}{\faBullseye}
```

> 图标随便换，`fontawesome5` 提供 1500+ 图标。注意：`*Alt` 后缀的图标在 TeXLive 中没有别名，要用星号变体（如 `\faFile*` `\faCalendar*` `\faMapMarker*` `\faExternalLink*`）。

---

## 4. 教育 / 工作 / 科研条目

```latex
% 教育（5 个必填 + 1 个可选 logo）
\educationItem[\tsinghuaLogo]{清华大学}{2023.09 -- 2026.06}{计算机}{硕士 · 排名 5%}

% 工作 / 实习 / 科研
\experienceItem[\tencentLogo]{腾讯 AI Lab}{2023.06 -- 2024.03}{算法实习生}{%
\begin{itemize}
  \item 工作内容 1（带量化指标）
  \item 工作内容 2
\end{itemize}
}
```

---

## 5. 项目卡片（5 个参数，全必填）

```latex
\projectCard{自我纠错型 RAG 系统}{2024.01 -- 2024.05}
{企业知识库 Agent，召回率 65% → 85%}                 % 一句话概述
{                                                     % itemize 详细
\begin{itemize}
  \item \textbf{技术栈}：LangChain、Qdrant、bge-reranker
  \item \textbf{核心方案}：迭代式检索 + 混合检索 + 重排序
  \item \textbf{效果}：用户满意度 82%，平均检索轮次 1.3
\end{itemize}
}
{\faGithub\ github.com/xxx/repo \quad \faGlobe\ demo.xxx.com}   % 链接 footer，可空 {}
```

---

## 6. 开源项目

```latex
\openSourceItem{huggingface/transformers}{135k}{27k}{Python}
{HuggingFace 主仓库 · contributor}
{%
\begin{itemize}
  \item 修复 Trainer.evaluate FSDP OOM 问题（PR #28xxx）
  \item 补充 Qwen2 长文本评测脚本
\end{itemize}
}
```

---

## 7. 作品集

```latex
\workItem{Hertz · 个人博客}{Hexo · 100k+ 阅读}
{https://blog.hertz.dev}
{长期撰写 LLM / Agent / RAG 系列原创长文 50+ 篇。}
```

---

## 8. 论文 / 荣誉

```latex
\publicationItem
{Hierarchical Knowledge Distillation for Compact LLMs}
{\textbf{Hertz}, Li Si, Wang Wu}
{NeurIPS 2024 (CCF-A)}
{\href{https://arxiv.org/abs/2410.xxxxx}{\faFilePdf\ Paper}\quad
 \href{https://github.com/xxx}{\faGithub\ Code}}

\awardItem{Kaggle LLM Science Exam · 金牌}{2023.08}{Top 1\% (128/2664)}
```

---

## 9. 技能可视化

```latex
% 进度条（0-10）
\skillbar{Python · PyTorch}{9}
\skillbar{大模型微调（LoRA / RLHF）}{8}

% 五点等级（1-5）
\skilldots{中文（母语）}{5}
\skilldots{英文（CET-6）}{4}

% 标签云
\skilltagAccent{LLM} \skilltag{RAG} \skilltag{Agent} \skilltag{LoRA} \skilltag{vLLM}

% GitHub 风格徽章
\badge{Stars}{562} \badge{License}{MIT} \badge{Build}{passing}
```

---

## 10. 摘要 / 自我评价

```latex
\begin{abstract}
计算机硕士在读，主攻大模型方向；NeurIPS 一作 1 篇，Kaggle 金牌；
具备完整数据 → 训练 → 推理部署经验。
\end{abstract}
```

---

## 11. Logo 短宏（在 `config.tex` 注册）

```latex
\def\tsinghuaLogo{logos/tsinghua.png}
\def\tencentLogo{logos/tencent.png}
\def\bytedanceLogo{logos/bytedance.png}
% ... 然后在模块中：
\experienceItem[\tencentLogo]{腾讯}{...}{...}{...}
```

---

## 12. Makefile 编译命令

```bash
make             # 主简历 → resume-pro-zh.pdf
make preview     # 主题预览 → themes-preview.pdf
make quickstart  # 极简示例 → quickstart.pdf
make all-pdf     # 全部 PDF
make watch       # 自动重编译
make lint        # LaTeX 语法检查（chktex）
make logos       # 重新生成占位 Logo（PNG）
make logos-svg   # 重新生成占位 Logo（PNG + SVG）
make clean       # 清理中间文件
make distclean   # 清理 + 删 PDF
```

---

## 13. v3.3+ 新增原语

```latex
% 页脚 QR 码（在 config.tex 中设置）
\qrlink{https://hertz.dev}

% 页数限制（超出时终端警告）
\setMaxPages{1}

% 仅首页渲染（如摘要只在第一页显示）
\rpIfPageOne{这部分内容只在第一页出现}

% 主题色分割线
\hdiv

% 高亮文本标签
\hltext{重点关键词}

% 日期范围快捷
\daterange{2023.09}{2026.06}

% 条件章节（show / hide / compact-only）
\conditionalSection[show]{章节标题}{\faIcon}{内容}
\conditionalSection[compact-only]{自我评价}{\faUserCheck}{...}  % 仅 compact 模式显示
\conditionalSection[hide]{求职意向}{\faBullseye}{...}           % 隐藏

% 证书条目（v3.5 新增）
\certItem{AWS Solutions Architect}{Amazon Web Services}{2024.03}

% 通用简历条目（v3.5 新增）
\resumeItem{技术分享}{2024}{在 NeurIPS Workshop 做关于模型压缩的 invited talk}

% 最后更新日期（v3.5 新增，自动中英文）
\lastupdated   % 中文：最后更新：YYYY年M月D日  英文：Last updated: Month DD, YYYY

% 水印（v3.5 新增，如 DRAFT / CONFIDENTIAL）
\watermark{DRAFT}

% Debug 模式（v3.5 新增，显示文本边界框 + 溢出标记）
% \documentclass[zh,debug]{resume-pro}
```

---

## 调整章节顺序 / 隐藏章节

打开 `resume-pro-zh.tex`，调整 `\input` 顺序即可：

```latex
\input{modules/header.tex}
\input{modules/skills.tex}
\input{modules/education.tex}
\input{modules/experience.tex}
\input{modules/projects.tex}
\input{modules/publications.tex}
% \input{modules/summary.tex}    % ← 注释这行就隐藏
```
