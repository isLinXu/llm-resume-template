# Logo 资源目录

把机构 / 公司 / 学校 Logo 放进此目录，然后在 `../config.tex` 中注册短宏：

```latex
\def\tsinghuaLogo{logos/tsinghua.png}
\def\tencentLogo{logos/tencent.png}
```

## 推荐规格

- **格式**：PNG（带透明背景，最佳）/ JPG / PDF
- **尺寸**：≥ 256 × 256，方形
- **背景**：透明（PNG）或与简历底色一致
- **命名**：小写 + 简短，例如 `tsinghua.png` `bytedance.png`

## 推荐获取方式

1. 官方品牌页（清华、Tencent、ByteDance、Alibaba 等公司多有官方资源页）
2. Wikipedia 媒体库（`File:XXX_logo.svg`，可下载 SVG 转 PNG）
3. simpleicons.org（仅图标，无文字）

## 占位图生成

`build_placeholders.py` 可自动生成占位 Logo（圆角方形 + 品牌色背景 + 首字母）：

```bash
# 默认生成 PNG
python3 build_placeholders.py

# 同时生成 SVG
python3 build_placeholders.py --svg

# 仅 SVG
python3 build_placeholders.py --only svg

# 自定义尺寸
python3 build_placeholders.py --size 512

# 自定义输出目录
python3 build_placeholders.py --output /path/to/out
```

### 当前支持的机构（50+）

**中国高校**：清华、北大、上海交大、浙大、复旦、中科大、中科院、哈工大、南大、武大、华科、中山大学、人大、地大、西南交大、川大、南开、天大、大连理工、电子科大、苏大、厦大、湖大、中南

**国际高校**：Stanford、MIT、ETH、Cambridge、Oxford、CMU、Berkeley、Princeton、Caltech、Columbia、UPenn、NYU、USC、UCLA、UCB、UIUC、Georgia Tech、UMich、UW、UCSD、UCI、UCD、UCSB、UCR、UCSC、UCM

**科技公司**：腾讯、字节跳动、阿里巴巴、百度、美团、华为、小米、滴滴、NVIDIA、OpenAI、Google、Microsoft、Amazon、Apple、Meta、Anthropic、DeepSeek、Moonshot、MiniMax、阿里云

## 在简历中使用

```latex
\educationItem[\tsinghuaLogo]{清华大学}{2023.09 -- 2026.06}{计算机科学与技术}{硕士}
\experienceItem[\tencentLogo]{腾讯 AI Lab}{2023.06 -- 2024.03}{算法实习生}{...}
```

未提供 Logo 时（`\def\tsinghuaLogo{}`），会自动渲染默认图标（`\faUniversity` / `\faBuilding`）。
