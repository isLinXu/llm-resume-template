# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.7.0] - 2026-06-15

### Added — 在线编辑器（GitHub Pages）
- **editor.html**：全新在线简历编辑器
  - 表单编辑器 + 代码编辑器双模式切换
  - LaTeX 语法高亮（命令/环境/注释/花括号分色）
  - 11 种变体一键切换（含快速入门）
  - 8 套主题色块预览 + 自定义三色
  - 语言/紧凑/单色/页脚可视化配置开关
  - 6 个模块独立开关切换
  - 侧栏个人信息表单（姓名/联系方式/链接）
  - 撤销/重做（50 步历史记录）
  - 搜索/替换（正则 + 单个/全部替换）
  - 可拖拽分割线（编辑区与预览区比例调整）
  - 1.2s 防抖自动保存到 localStorage
  - 键盘快捷键（Ctrl+S / Ctrl+1-7 / Ctrl+Enter / ?）
  - GitHub API 一键提交修改并触发 CI 构建
  - ZIP 打包下载（JSZip）+ PDF 直接下载
  - 实时字符数 + 行数显示
  - Tab 缩进支持
  - 拖放文件导入（.tex / .json）
  - 导入/导出配置（JSON 格式）
  - 版本指示器
  - prefers-reduced-motion 支持
  - localStorage 配额检查
- **preview.html**：全新 PDF 预览页
  - 13 个 PDF 选项（主简历 + 10 变体 + 快速入门 + 主题预览）
  - 缩略图侧栏导航
  - 适应宽度按钮
  - 全屏模式
  - Ctrl+滚轮缩放
  - 打印支持
  - Home/End 键跳转
  - Toast 通知
  - 备用路径加载
- **index.html**：全新着陆页
  - 渐变背景 Hero 区
  - 毛玻璃导航栏
  - 9 张特性卡片
  - 11 种变体展示区
  - 彩色目录树架构图
  - 滚动入场动画
  - 浮动粒子背景
  - 渐变文字动画
  - 移动端汉堡菜单
  - 方案对比表格
  - FAQ 手风琴
  - 回到顶部按钮
  - 结构化数据（JSON-LD）
- **sw.js**：Service Worker 离线支持
  - 网络优先 + 缓存回退策略
  - 自动清理旧版本缓存
  - 跳过 PDF 请求（始终从网络获取）

### Changed — CI/CD
- **pages.yml**：添加 `timeout-minutes`、Verify builds 步骤、`[skip ci]` 防循环触发、修复缺失的 `permissions` 关键字
- **build.yml**：添加 `timeout-minutes`、Verify builds 步骤（写入 `$GITHUB_STEP_SUMMARY`）、`[skip ci]` 防循环触发、TeX 缓存优化
- **config.tex**：版本号更新至 v3.7.0

### Fixed
- **editor.html**：修复 `classfld"` 损坏属性为 `class="fld"`
- **editor.html**：添加 `<script type="module">` 支持，引入 JSZip 实现真正 ZIP 下载（含 fallback 降级机制）
- **editor.html**：修复 Ctrl+Z/Y/F/1-7 在输入框中误触发的问题
- **editor.html**：修复 `esc()` 函数缺少单引号转义（XSS 风险）
- **editor.html**：修复 `delEdu/delExp/delProj/delPub/delAward` 在项目不存在时仍执行 markMod/saveLS/histPush 的问题
- **editor.html**：修复 `updEduField` 在 educationItem 包含 itemize 块时替换逻辑错误
- **editor.html**：修复 `updExpField` 使用正则替换导致 itemize 块丢失的问题，改为解析重建
- **editor.html**：修复 `updProjField` 使用正则替换导致字段错位的问题，改为解析重建
- **editor.html**：修复 `updPubField/updAwardField` 使用正则替换导致格式丢失的问题，改为解析重建
- **editor.html**：修复 `updSkillRow` 使用 replace 导致特殊字符问题，改为 indexOf 精确替换
- **editor.html**：修复 `updCfg` 在输入时调用 syncFormFromConfig 导致光标重置的问题
- **editor.html**：修复 `syncCfg` 缺少 histPush 调用导致无法撤销的问题
- **editor.html**：修复表单模式切换回代码模式时编辑器内容不同步的问题
- **preview.html**：修复键盘快捷键在输入框中误触发的问题
- **preview.html**：修复 `enterFS` 传递错误字符串参数给 renderPage 的问题
- **preview.html**：修复 `renderPage` 未使用的 targetArea 参数
- **index.html**：修复版本号不一致（v3.6.1 → v3.7.0）
- **index.html**：添加 robots meta 标签
- **pages.yml**：修复缺失的 `permissions:` 关键字
- **pages.yml**：修复 Verify builds 步骤使用 macOS stat 语法的问题
- **pages.yml**：添加 `[skip ci]` 检查防止 build.yml 提交 PDF 时循环触发
- **editor.html**：修复 `esc()` 缺少反引号转义（XSS 风险）
- **editor.html**：修复 `updCfg` 中 val 包含特殊字符时正则替换失败的问题
- **editor.html**：修复 `syncCfg` 空值覆盖已有配置的问题
- **editor.html**：修复 `setVariant` 缺少 histPush 导致变体切换无法撤销
- **editor.html**：修复 Ctrl+B/J 在输入框中误触发
- **editor.html**：修复 `doReplaceAll` 空搜索字符串导致无限循环
- **editor.html**：修复 `doReplace` 缺少保存和历史记录
- **editor.html**：修复 `genMainTex` 不考虑语言设置的问题
- **editor.html**：修复 `highlightLatex` 注释匹配不精确（`%.+` → `%[^\n]*`）
- **editor.html**：修复 `fmtCode` 过于激进的格式化（在 `\begin{}` 前强制换行）
- **editor.html**：修复 `build()` 缺少 GitHub API 错误处理
- **editor.html**：修复 `dlPDF()` 无 GitHub 配置时只提示不提供替代方案
- **editor.html**：修复 `checkBuild` 只检查一次不轮询 CI 状态
- **editor.html**：修复 `renderExpForm`/`renderProjForm` 正则第四字段无法匹配含 `}` 的内容
- **editor.html**：修复 `addExp` 缺少闭合大括号换行
- **editor.html**：修复 `updExpField` 重建格式缺少换行
- **editor.html**：修复 `renderConfigForm` 缺少 wechat/zhihu 字段
- **editor.html**：修复 undo/redo 在表单模式下不更新表单
- **preview.html**：修复 `esc()` 缺少引号转义
- **preview.html**：修复 `printPDF` 的 onload 跨域问题
- **preview.html**：修复键盘快捷键 Ctrl+组合键冲突
- **sw.js**：修复 PDF 路径匹配不够精确（`/pdfs/` → `.pdf`）
- **build.yml**：修复 `git add` 与 `.gitignore` 冲突（添加 `-f` 强制添加）

## [3.6.1] - 2026-06-06

### Fixed
- **横线间距不一致**：统一所有条目类型（`\educationItem`、`\experienceItem`、`\projectCard`、`\openSourceItem`、`\workItem`、`\publicationItem`、`\resumeItem`）的 `\vspace` 前间距为 `0.2em`，`\awardItem`/`\certItem` 为 `0.15em`，消除 section 分割线与内容间距不统一的问题
- **section 标题间距**：`\titlespacing*` 上方从 `1.0ex` 缩减至 `0.8ex`，下方从 `0.4ex` 缩减至 `0.3ex`，使横线与标题更紧凑

## [3.6.0] - 2026-06-06

### Added
- **头部渐变分割线**：Header 底部分割线改为 TikZ 渐变效果（左深右浅），增强视觉层次
- **头像主题色细边框**：圆形/圆角头像增加 `themecolor!40` 细边框，提升精致感
- **技能进度条渐变填充**：`\skillbar` 进度条从纯色改为 `themecolor → accentcolor` 渐变
- **技能标签微阴影**：`\skilltag` 增加 `lightcolor!50` 浅底填充，`\skilltagAccent` 增加 `drop shadow`
- **徽章微阴影**：`\badge` 右侧标签增加 `drop shadow` 效果
- **摘要左侧装饰线**：`abstract` 环境增加 `themecolor!40` 竖线装饰
- **论文条目左侧装饰线**：`\publicationItem` 增加 `themecolor!30` 竖线装饰
- **荣誉条目左侧装饰线**：`\awardItem` 增加 `accentcolor!30` 竖线装饰
- **TikZ `fadings` + `shadows` 库**：支持渐变和阴影效果

### Changed
- **姓名字号**：从 20pt 增大到 22pt，行高从 24pt 增大到 26pt
- **标语颜色**：从 `darkcolor` 改为 `mutedcolor`，更柔和
- **超链接颜色**：`urlcolor` 从 `themecolor` 改为 `accentcolor`，区分链接与标题
- **页面几何**：非 compact 模式 top 从 1.2cm 减至 1.0cm，compact 模式 top 从 1.0cm 减至 0.8cm
- **版本号**：v3.5.0 → v3.6.0

## [3.5.0] - 2026-06-06

### Added
- **`resume-pro.cls` v3.5**：新增 `[debug]` 类选项（显示文本边界框 + 溢出标记）
- **`\certItem{证书名}{颁发机构}{时间}`**：证书条目原语
- **`\resumeItem{标题}{时间}{描述}`**：通用简历条目原语
- **`\lastupdated`**：自动中英文「最后更新」日期
- **`\watermark{文本}`**：水印支持（如 DRAFT / CONFIDENTIAL）
- **`docker-compose.yml`**：Docker Compose 简化编译
- **`.gitattributes`**：Git 属性配置（二进制检测 / 换行符 / 语言识别）
- **`build_variants.sh`**：支持 `-j N` 并行编译

### Fixed
- **`resume-pro.cls`**：`\rp@ifdefshow` 定义位置移至 `\makeheader` 之前（修复潜在前向引用问题）
- **`resume-pro.cls`**：消除 `fancyfoot` 代码重复，提取 `\rp@footerright` 内部宏
- **`modules-en/skills.tex`**：修复两个 `\skillrow{Languages}` 重复标签（改为 `Programming` / `Natural Languages`）
- **`variant-english.tex`**：移除冗余 Logo 定义，改用 `\input{config.tex}` 统一加载
- **CI `build.yml`**：移除错误的 `pip install chktex`（chktex 已包含在 TeX Live 中）

### Changed
- **`Dockerfile`**：补装 `fonts-ibm-plex`（西文首选字体）
- **`README.md`**：添加 Overleaf 按钮、debug 模式 FAQ、新命令速查
- **`CHEATSHEET.md`**：补充 v3.5 新增原语说明
- **`Makefile`**：`make variants` 支持并行编译

## [3.4.1] - 2026-06-06

### Fixed
- **`resume-pro.cls`**：修复字体回退链 `\IfFontExistsTF` 嵌套括号不匹配导致编译失败的问题（`Too many }'s`）
- **`CHANGELOG.md`**：删除 v3.4 下重复的 v3.3 `### Changed` 段落
- **`README.md`**：将 badge URL 中的 `yourname` 替换为 `YOUR_GITHUB_USERNAME` 并添加 TODO 注释
- **`config.tex`**：添加醒目的占位数据替换警告（⚠️ 标记）

### Changed
- **`logos/`**：首次生成 72 个 SVG 格式 Logo 占位图（与 PNG 配套）

### Verified
- 通过 Docker（`danteev/texlive:latest`）XeLaTeX 编译验证全部 12 个 PDF：
  - `resume-pro-zh.pdf`（2 页）、`quickstart.pdf`（1 页）、`themes-preview.pdf`（1 页）
  - 9 套变体全部编译通过（academic / academic-long / blackpro / coverletter / english / minimalist / onepage / product / purple / twocolumn）

## [3.4.0] - 2026-06-05

### Added
- **版本号更新至 v3.4**
- **`resume-pro.cls` v3.4**：新增 QR 码（`qrcode` 宏包）、页数溢出警告（`\setMaxPages`）、条件渲染（`\rpIfPageOne`）、实用原语（`\hdiv`、`\hltext`、`\daterange`）
- **`config.tex`**：新增 `\qrlink` 和 `\setMaxPages` 配置段
- **`build_placeholders.py` v3.4**：
  - 支持 SVG 输出（`--svg` / `--only svg`）
  - 自定义尺寸（`--size`）和输出目录（`--output`）
  - 新增 15+ 机构 Logo 占位图（含品牌色 + 首字母缩写）
- **Makefile v3.4**：
  - `make lint`：使用 chktex 进行 LaTeX 语法检查
  - `make logos-svg`：同时生成 PNG 和 SVG 格式的 Logo
  - `make all-pdf`：一键构建所有变体 PDF
- **GitHub Actions v3.4**：
  - PR 评论中自动附加构建结果表格
  - Job Summary 中显示 PDF 文件大小
  - Tag 触发时自动创建 GitHub Release

### Changed
- **`resume-pro.cls`** 版本升级至 v3.4
- **`config.tex`** 新增 `\qrlink` 和 `\setMaxPages` 配置段
- **`build_placeholders.py`** 加入 `variant-onepage.tex` 到批量编译流程
- **`variants/README.md`** 更新为 9 套变体文档
- **`logos/README.md`** 补充 SVG 用法和完整机构列表
- **`CHEATSHEET.md`** 补充 v3.4 新增原语说明

## [3.2.0] - 2026-06-05

### Added
- **GitHub Actions CI/CD** (`.github/workflows/build.yml`): 自动构建所有 PDF，push 到 main 时自动提交产物
- **Dockerfile**: 基于 `danteev/texlive` 的可复现构建环境，含中文字体
- **`.latexmkrc`**: 统一 latexmk 编译配置，`make watch` 更稳定
- **`variant-academic-long.tex`**: 长版学术 CV 变体（3+ 页），含研究兴趣、学术服务、教学经历、学术交流等章节
- **根目录 `README.md`**: 项目门面文档，含完整特性表、项目结构、Docker 用法
- **`LICENSE`**: MIT 许可证
- **`CHANGELOG.md`**: 版本变更记录

### Changed
- **`build_placeholders.py`**: 跨平台字体检测（macOS / Linux / Windows），Pillow ≥ 10.0 兼容
- **`build_variants.sh`**: 新增 `variant-academic-long.tex` 到批量编译列表
- **`variants/README.md`**: 更新为 8 套变体文档，含双栏和求职信说明
- **`.gitignore`**: 大幅扩充，覆盖 LaTeX 全量中间文件、Docker、Python 缓存等

## [3.1.0] - 2025-05-20

### Added
- 紧凑专业版样式（v3.1）：章节标题 11pt SmallCaps + 0.4pt 细线
- 卡片去 tcolorbox 填充，改为粗体标题 + 时间右对齐 + 列表
- 头部支持 圆形 / 方形 / 圆角 头像 + 顶部右侧品牌 Logo
- 教育 / 工作条目支持 Logo（自动缩放对齐）
- 页眉页脚（fancyhdr）：左姓名、中页码、右更新日期
- 8 套内置主题色
- 7 套场景变体（学术 / 商务 / 极简 / 产品 / 双栏 / 英文 / 求职信）
- 中英文模块分离（`modules/` + `modules-en/`）
- `CHEATSHEET.md` 命令速查表
- `quickstart.tex` 极简入门示例
- `themes-preview.tex` 主题视觉规范预览
- `build_placeholders.py` Logo 占位图自动生成（25+ 机构）
- `Makefile` 一键编译脚本

## [3.0.0] - 2024-12-15

### Added
- 初始版本：模块化 LaTeX 简历模板
- 核心样式类 `resume-pro.cls`
- 集中配置 `config.tex`
- 模块化章节 `modules/*.tex`
