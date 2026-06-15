# Contributing to LLM Resume Template

感谢你对本项目的关注！无论是修复 bug、增加新主题、添加新模块，还是改善文档，都非常欢迎。

---

## 🚀 快速贡献流程

1. **Fork** 本仓库
2. 创建分支：`git checkout -b feat/my-feature`
3. 编辑并测试（确保 `make all-pdf` 通过）
4. 提交：`git commit -m "feat: add XXX"`
5. 推送：`git push origin feat/my-feature`
6. 创建 Pull Request

---

## 📐 贡献方向

### 1. 新主题色

在 `resume-pro.cls` 中添加：

```latex
\newcommand{\theme@yourname}{\rp@settheme{主色HEX}{次色HEX}{浅底HEX}}
```

同时在 `README.md` 主题表中补充一行。

### 2. 新模块

在 `modules/` 或 `modules-en/` 下新建 `.tex` 文件，使用已有的原语（`\sectionTitle`、`\experienceItem` 等）。然后在主文件中添加对应的 `\input{modules/xxx.tex}`。

### 3. 新变体

在 `variants/` 下新建 `variant-yourname.tex`，参考现有变体的结构。别忘了：

- 在 `build_variants.sh` 的 `VARIANTS` 数组中添加条目
- 在 `variants/README.md` 中补充说明

### 4. 字体兼容性

改善 `resume-pro.cls` 中的字体回退逻辑，特别是 Linux 发行版的默认中文字体支持。

### 5. 文档改善

修正拼写、补充示例、改善中英文翻译一致性等。

---

## ✅ 提交规范

使用 [Conventional Commits](https://www.conventionalcommits.org/) 格式：

| 类型 | 说明 |
|---|---|
| `feat:` | 新功能（新主题、新模块、新变体） |
| `fix:` | Bug 修复 |
| `docs:` | 文档改善 |
| `style:` | 排版 / 格式调整（不影响逻辑） |
| `refactor:` | 代码重构 |
| `ci:` | CI/CD 相关 |

---

## 🧪 测试清单

提交 PR 前，请确保以下检查通过：

- [ ] `make all-pdf` 编译成功（无 fatal error）
- [ ] 新增的 `.tex` 文件在 `xelatex` 两遍编译后正常渲染
- [ ] 如果修改了 `resume-pro.cls`，确保现有变体不受影响
- [ ] 如果添加了新 Logo，确保 `build_placeholders.py` 正常生成
- [ ] 如果修改了英文字体回退逻辑，确保 `[en]` 模式正常

---

## 📁 项目结构约定

```
latex_resume_pro/
├── resume-pro.cls      # 核心：样式类（修改需谨慎）
├── config.tex           # 用户配置入口
├── modules/             # 中文模块
├── modules-en/          # 英文模块
├── variants/            # 场景变体
└── logos/               # Logo 占位图 + 生成脚本
```

- **`resume-pro.cls`** 是公共 API，修改需向后兼容
- **`modules/`** 是用户最常编辑的区域，保持简洁
- **`variants/`** 各变体应独立可编译

---

## ❓ 有疑问？

- 先查阅 [README.md](README.md) 和 [CHEATSHEET.md](latex_resume_pro/CHEATSHEET.md)
- 在 GitHub Issues 中搜索类似问题
- 如果找不到答案，新建 Issue 并附上最小复现代码

感谢你的贡献！🎉
