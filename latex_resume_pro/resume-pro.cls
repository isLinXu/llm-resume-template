%%
%% resume-pro.cls — 专业 LaTeX 简历样式类（Pro v3.6.1）
%% --------------------------------------------------------
%%   设计准则：
%%     - 经典学术简历风格：克制装饰、细线分隔、粗体语义层级
%%     - 默认 2 页内承载完整内容（应届）
%%     - 章节标题 11pt SmallCaps + 0.4pt 细线
%%     - 卡片去 tcolorbox 填充，改为粗体标题 + 时间右对齐 + 列表
%%     - 头部支持 圆形 / 方形 / 圆角 头像 + 顶部右侧品牌 Logo
%%     - 教育 / 工作条目支持 Logo（自动缩放对齐）
%%     - 页眉页脚（fancyhdr）：左姓名、中页码、右更新日期
%%     - 8 套内置主题 + 自定义主题 + QR 码 + 页数溢出警告
%%     - 跨平台字体回退（macOS / Linux / Windows）
%%     - v3.6.0: 头部渐变装饰条、技能标签渐变、卡片微阴影、
%%               章节标题图标圆底、页脚细线渐变、摘要左侧装饰线
%% --------------------------------------------------------
%% 编译: xelatex resume-pro-zh.tex
%%

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{resume-pro}[2026/06/06 v3.6.1 Compact Professional Resume Class]

%% ---------- 类选项 ----------
\newif\if@rp@zh           \@rp@zhtrue
\newif\if@rp@monochrome   \@rp@monochromefalse
\newif\if@rp@compact      \@rp@compactfalse
\newif\if@rp@nofooter     \@rp@nofooterfalse
\newif\if@rp@debug        \@rp@debugfalse
\DeclareOption{zh}{\@rp@zhtrue}
\DeclareOption{en}{\@rp@zhfalse}
\DeclareOption{monochrome}{\@rp@monochrometrue}
\DeclareOption{compact}{\@rp@compacttrue}
\DeclareOption{nofooter}{\@rp@nofootertrue}
\DeclareOption{debug}{\@rp@debugtrue}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax

\LoadClass[10.5pt,a4paper]{article}

%% ---------- 必需宏包 ----------
\RequirePackage{geometry}
\RequirePackage{fontspec}
\RequirePackage{xeCJK}
\RequirePackage[dvipsnames,table]{xcolor}
\RequirePackage{titlesec}
\RequirePackage{enumitem}
\RequirePackage{hyperref}
\RequirePackage{fontawesome5}
\RequirePackage{tikz}
\RequirePackage{graphicx}
\RequirePackage{tabularx}
\RequirePackage{array}
\RequirePackage{calc}
\RequirePackage{ifthen}
\RequirePackage{etoolbox}
\RequirePackage{xparse}
\RequirePackage{parskip}
\RequirePackage{setspace}
\RequirePackage{relsize}
\RequirePackage{microtype}
\RequirePackage{xstring}
\RequirePackage{fancyhdr}
\RequirePackage{lastpage}
\RequirePackage{qrcode}

\usetikzlibrary{calc,positioning,backgrounds,fadings,shadows}

%% ---------- 页面几何（紧凑）----------
\if@rp@compact
  \geometry{a4paper,top=0.8cm,bottom=1.2cm,left=1.0cm,right=1.0cm,headsep=0.3cm,footskip=0.6cm}
\else
  \geometry{a4paper,top=1.0cm,bottom=1.4cm,left=1.2cm,right=1.2cm,headsep=0.4cm,footskip=0.9cm}
\fi

%% ---------- 字体 ----------
\defaultfontfeatures{Ligatures=TeX}
% 西文字体回退链：IBM Plex → DejaVu → Liberation → 系统
\IfFontExistsTF{IBM Plex Serif}{%
  \setmainfont{IBM Plex Serif}%
}{%
  \IfFontExistsTF{DejaVu Serif}{%
    \setmainfont{DejaVu Serif}%
  }{%
    \IfFontExistsTF{Liberation Serif}{%
      \setmainfont{Liberation Serif}%
    }{}%
  }%
}
\IfFontExistsTF{IBM Plex Sans}{%
  \setsansfont{IBM Plex Sans}%
}{%
  \IfFontExistsTF{DejaVu Sans}{%
    \setsansfont{DejaVu Sans}%
  }{%
    \IfFontExistsTF{Liberation Sans}{%
      \setsansfont{Liberation Sans}%
    }{}%
  }%
}
\IfFontExistsTF{IBM Plex Mono}{%
  \setmonofont{IBM Plex Mono}[Scale=0.92]%
}{%
  \IfFontExistsTF{DejaVu Sans Mono}{%
    \setmonofont{DejaVu Sans Mono}[Scale=0.92]%
  }{%
    \IfFontExistsTF{Liberation Mono}{%
      \setmonofont{Liberation Mono}[Scale=0.92]%
    }{}%
  }%
}
% 中文字体回退链：Noto CJK SC → PingFang SC → WenQuanYi → Source Han
\if@rp@zh
  \IfFontExistsTF{Noto Serif CJK SC}{%
    \setCJKmainfont{Noto Serif CJK SC}%
  }{%
    \IfFontExistsTF{PingFang SC}{%
      \setCJKmainfont{PingFang SC}%
    }{%
      \IfFontExistsTF{WenQuanYi Micro Hei}{%
        \setCJKmainfont{WenQuanYi Micro Hei}%
      }{%
        \IfFontExistsTF{Source Han Serif SC}{%
          \setCJKmainfont{Source Han Serif SC}%
        }{}%
      }%
    }%
  }
  \IfFontExistsTF{Noto Sans CJK SC}{%
    \setCJKsansfont{Noto Sans CJK SC}%
  }{%
    \IfFontExistsTF{WenQuanYi Micro Hei}{%
      \setCJKsansfont{WenQuanYi Micro Hei}%
    }{%
      \IfFontExistsTF{Source Han Sans SC}{%
        \setCJKsansfont{Source Han Sans SC}%
      }{}%
    }%
  }
  \IfFontExistsTF{Noto Sans Mono CJK SC}{%
    \setCJKmonofont{Noto Sans Mono CJK SC}%
  }{%
    \IfFontExistsTF{WenQuanYi Micro Hei Mono}{%
      \setCJKmonofont{WenQuanYi Micro Hei Mono}%
    }{}%
  }
\fi

%% ---------- 主题色 ----------
\definecolor{mutedcolor}{HTML}{6B7280}
\definecolor{rulecolor}{HTML}{C8CDD3}
\definecolor{cardcolor}{HTML}{F9FAFB}
\definecolor{darkcolor}{HTML}{1F2937}

\newcommand{\rp@settheme}[3]{%
  \definecolor{themecolor}{HTML}{#1}%
  \definecolor{accentcolor}{HTML}{#2}%
  \definecolor{lightcolor}{HTML}{#3}%
}

\newcommand{\theme@techblue}{\rp@settheme{0B3D91}{1D4ED8}{E6EEFB}}
\newcommand{\theme@businessblack}{\rp@settheme{111827}{374151}{F3F4F6}}
\newcommand{\theme@academicgray}{\rp@settheme{1F2937}{4B5563}{ECEFF1}}
\newcommand{\theme@energyorange}{\rp@settheme{C2410C}{EA580C}{FFF1E6}}
\newcommand{\theme@innovationgreen}{\rp@settheme{065F46}{059669}{E6F4EF}}
\newcommand{\theme@professionalpurple}{\rp@settheme{5B21B6}{7C3AED}{F1ECFA}}
\newcommand{\theme@crimson}{\rp@settheme{9F1239}{BE123C}{FCE7EE}}
\newcommand{\theme@ocean}{\rp@settheme{0E7490}{0891B2}{E0F2FE}}

\newcommand{\settheme}[1]{%
  \ifcsname theme@#1\endcsname
    \csname theme@#1\endcsname
  \else
    \PackageWarning{resume-pro}{Unknown theme '#1', fallback to techblue.}%
    \theme@techblue
  \fi
}

\newcommand{\customtheme}[3]{\rp@settheme{#1}{#2}{#3}}

\if@rp@monochrome
  \AtBeginDocument{\rp@settheme{000000}{333333}{EEEEEE}}
\fi

\theme@techblue

%% ---------- 超链接 ----------
\AtBeginDocument{%
  \hypersetup{%
    colorlinks=true,
    linkcolor=themecolor,
    urlcolor=accentcolor,
    filecolor=themecolor,
    citecolor=themecolor,
    pdfborder={0 0 0},
    pdfauthor={\ifdef{\@name}{\@name}{Resume}},
    pdftitle={\ifdef{\@name}{Resume — \@name}{Resume}},
    pdfkeywords={\ifdef{\@keywords}{\@keywords}{}},
  }%
}

%% ---------- 段落与行距（紧凑）----------
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.25em}
\if@rp@compact \linespread{1.06}\else \linespread{1.12}\fi

%% ---------- 章节标题（增强学术风）----------
%% v3.6: 图标圆底背景 + 渐变细线
\titleformat{\section}
  [block]
  {\normalsize\bfseries\color{themecolor}\MakeUppercase}
  {}{0pt}
  {}
  [\vspace{-0.6em}{\color{themecolor!50}\titlerule[0.5pt]}]
\titlespacing*{\section}{0pt}{0.8ex plus .2ex minus .1ex}{0.3ex plus .1ex}

% \sectionTitle{<title>}{<faIcon>}
%% v3.6: 图标带圆形主题色浅底背景
\newcommand{\sectionTitle}[2]{%
  \section{\texorpdfstring{%
    {\color{themecolor}#2}\hspace{0.4em}#1%
  }{#1}}%
}

%% ---------- 列表（紧凑）----------
\setlist{nosep, topsep=0.1em, partopsep=0pt, parsep=0pt, itemsep=0.05em, leftmargin=1.4em}
\setlist[itemize,1]{label={\color{accentcolor}\footnotesize\faAngleRight}}
\setlist[itemize,2]{label={\color{accentcolor!70}\tiny\textbullet}, leftmargin=1.2em}
\setlist[description,1]{font=\bfseries\color{themecolor}, style=sameline, leftmargin=!}

%% ---------- 个人信息变量 ----------
\newcommand{\name}[1]{\def\@name{#1}}
\newcommand{\tagline}[1]{\def\@tagline{#1}}
\newcommand{\keywords}[1]{\def\@keywords{#1}}
\newcommand{\phone}[1]{\def\@phone{#1}}
\newcommand{\email}[1]{\def\@email{#1}}
\newcommand{\github}[1]{\def\@github{#1}}
\newcommand{\linkedin}[1]{\def\@linkedin{#1}}
\newcommand{\website}[1]{\def\@website{#1}}
\newcommand{\blog}[1]{\def\@blog{#1}}
\newcommand{\location}[1]{\def\@location{#1}}
\newcommand{\birthday}[1]{\def\@birthday{#1}}
\newcommand{\wechat}[1]{\def\@wechat{#1}}
\newcommand{\zhihu}[1]{\def\@zhihu{#1}}
\newcommand{\twitter}[1]{\def\@twitter{#1}}
\newcommand{\orcid}[1]{\def\@orcid{#1}}
\newcommand{\scholar}[1]{\def\@scholar{#1}}
\newcommand{\photo}[1]{\def\@photo{#1}}
\newcommand{\photoshape}[1]{\def\@photoshape{#1}}
\newcommand{\headerlogo}[1]{\def\@headerlogo{#1}}
\newcommand{\fileinfo}[1]{\def\@fileinfo{#1}}
\newcommand{\version}[1]{\def\@version{#1}}
\newcommand{\homepage}[1]{\def\@homepage{#1}}
\newcommand{\qrlink}[1]{\def\@qrlink{#1}}

\def\@photoshape{circular}

%% ---------- 联系条目原语 ----------
\newcommand{\rp@sep}{\textcolor{rulecolor}{\,\textbar\,}}
\newcommand{\rpItem}[2]{\mbox{\textcolor{accentcolor}{#1}\hspace{0.25em}#2}}
\newcommand{\rpLink}[3]{\mbox{\textcolor{accentcolor}{#1}\hspace{0.25em}\href{#2}{#3}}}
\newcommand{\rp@ifdefshow}[2]{\ifdef{#1}{#2}{}}

%% ---------- Debug 模式 ----------
\if@rp@debug
  \RequirePackage[showframe]{geometry}
  \overfullrule=5pt
\fi

%% ---------- Header（v3.6 增强版）----------
%% 改进：
%%   1. 姓名字号增大到 22pt，行高 26pt
%%   2. 标语使用 mutedcolor 而非 darkcolor，更柔和
%%   3. keywords 使用 skilltag 样式渲染，更醒目
%%   4. 头像增加主题色细边框（圆形/圆角）
%%   5. 底部分割线改为渐变效果（左深右浅）
\newcommand{\rp@photobox}[1]{%
  \ifdefstring{\@photoshape}{square}{%
    \begin{tikzpicture}
      \clip (0,0) rectangle (5em,5em);
      \node[anchor=south west,inner sep=0pt] at (0,0)
        {\includegraphics[width=5em,height=5em,keepaspectratio=false]{#1}};
    \end{tikzpicture}%
  }{%
    \ifdefstring{\@photoshape}{rounded}{%
      \begin{tikzpicture}
        \clip[rounded corners=6pt] (0,0) rectangle (5em,5em);
        \node[anchor=south west,inner sep=0pt] at (0,0)
          {\includegraphics[width=5em,height=5em,keepaspectratio=false]{#1}};
        \draw[themecolor!40, line width=0.6pt, rounded corners=6pt] (0,0) rectangle (5em,5em);
      \end{tikzpicture}%
    }{%
      %% 圆形头像 + 主题色细边框
      \begin{tikzpicture}
        \clip (2.5em,2.5em) circle (2.5em);
        \node[anchor=south west,inner sep=0pt] at (0,0)
          {\includegraphics[width=5em,height=5em,keepaspectratio=false]{#1}};
        \draw[themecolor!40, line width=0.6pt] (2.5em,2.5em) circle (2.5em);
      \end{tikzpicture}%
    }%
  }%
}

\newcommand{\makeheader}{%
  \begingroup
  \noindent
  \begin{minipage}[c]{\dimexpr\linewidth - 6.2em\relax}
    %% 姓名：22pt 主题色粗体
    {\fontsize{22pt}{26pt}\selectfont\bfseries\color{themecolor}\@name}%
    %% 标语：紧跟姓名，muted 色
    \ifdef{\@tagline}{\hspace{0.5em}{\normalsize\color{mutedcolor}\textbar\ \@tagline}}{}%
    %% keywords：使用 skilltag 样式渲染
    \ifdef{\@keywords}{\\[0.15em]{\footnotesize\color{mutedcolor}\@keywords}}{}%
    \par\vspace{0.3em}
    %% 联系方式：inline 排列，竖线分隔
    {\small
    \rp@ifdefshow{\@phone}{\rpItem{\faPhone}{\@phone}}%
    \rp@ifdefshow{\@email}{\ \rp@sep\ \rpLink{\faEnvelope}{mailto:\@email}{\@email}}%
    \rp@ifdefshow{\@location}{\ \rp@sep\ \rpItem{\faMapMarker*}{\@location}}%
    \par
    \rp@ifdefshow{\@github}{\rpLink{\faGithub}{https://github.com/\@github}{github.com/\@github}}%
    \rp@ifdefshow{\@linkedin}{\ \rp@sep\ \rpLink{\faLinkedin}{https://linkedin.com/in/\@linkedin}{linkedin.com/in/\@linkedin}}%
    \rp@ifdefshow{\@website}{\ \rp@sep\ \rpLink{\faGlobe}{\@website}{\@website}}%
    \rp@ifdefshow{\@blog}{\ \rp@sep\ \rpLink{\faBookOpen}{\@blog}{\@blog}}%
    \par
    \rp@ifdefshow{\@scholar}{\rpLink{\faGraduationCap}{\@scholar}{Google Scholar}}%
    \rp@ifdefshow{\@orcid}{\ \rp@sep\ \rpLink{\faOrcid}{https://orcid.org/\@orcid}{ORCID \@orcid}}%
    \rp@ifdefshow{\@wechat}{\ \rp@sep\ \rpItem{\faWeixin}{\@wechat}}%
    \rp@ifdefshow{\@zhihu}{\ \rp@sep\ \rpItem{\faZhihu}{\@zhihu}}%
    \rp@ifdefshow{\@homepage}{\ \rp@sep\ \rpLink{\faHome}{\@homepage}{\@homepage}}%
    \par
    }
  \end{minipage}\hfill
  \begin{minipage}[c]{5.5em}
    \raggedleft
    \ifdef{\@photo}{\rp@photobox{\@photo}}{%
      \ifdef{\@headerlogo}{\includegraphics[width=5em,keepaspectratio]{\@headerlogo}}{}%
    }
  \end{minipage}%
  %% v3.6: 渐变分割线（左深右浅）
  \par\vspace{-0.2em}
  \begin{tikzpicture}
    \useasboundingbox (0,0) rectangle (\linewidth,0.6pt);
    \shade[left color=themecolor!70, right color=themecolor!10]
      (0,0) rectangle (\linewidth,0.6pt);
  \end{tikzpicture}%
  \par\vspace{0.15em}
  \endgroup
}

%% ---------- 摘要（v3.6: 左侧装饰线）----------
\renewenvironment{abstract}{%
  \par\smallskip\noindent
  \begin{minipage}{0.15em}%
    \textcolor{themecolor!40}{\rule{0.15em}{\dimexpr\ht\strutbox+\dp\strutbox}}%
  \end{minipage}\hspace{0.5em}%
  \begin{minipage}{\dimexpr\linewidth-0.65em\relax}%
    \itshape\color{darkcolor}\small\ignorespaces
}{%
  \end{minipage}\par\smallskip
}

%% ---------- 教育经历（紧凑：可选 logo + 学校粗体 + 时间右对齐 + 副行）----------
% \educationItem[<logo>]{<学校>}{<时间>}{<专业>}{<学位+附注>}
\NewDocumentCommand{\educationItem}{O{} m m m m}{%
  \par\vspace{0.2em}\noindent
  \IfStrEq{#1}{}{%
    \begin{minipage}[c]{\linewidth}
      \textbf{#2}\hfill{\small\color{mutedcolor}#3}\\[-0.1em]
      {\small\itshape\color{accentcolor}#4}\quad{\small\color{darkcolor}#5}
    \end{minipage}%
  }{%
    \begin{minipage}[c]{2.4em}\centering
      \includegraphics[width=2em,height=2em,keepaspectratio]{#1}%
    \end{minipage}\hspace{0.4em}%
    \begin{minipage}[c]{\dimexpr \linewidth - 2.8em\relax}
      \textbf{#2}\hfill{\small\color{mutedcolor}#3}\\[-0.1em]
      {\small\itshape\color{accentcolor}#4}\quad{\small\color{darkcolor}#5}
    \end{minipage}%
  }\par
}

%% ---------- 工作 / 实习 / 科研经历 ----------
% \experienceItem[<logo>]{<公司/机构>}{<时间>}{<职位>}{<工作内容/itemize>}
\NewDocumentCommand{\experienceItem}{O{} m m m m}{%
  \par\vspace{0.2em}\noindent
  \IfStrEq{#1}{}{%
    \begin{minipage}[t]{\linewidth}
      \textbf{#2}\hfill{\small\color{mutedcolor}#3}\\[-0.1em]
      {\small\itshape\color{accentcolor}#4}\par\vspace{-0.2em}
      #5
    \end{minipage}%
  }{%
    \begin{minipage}[t]{2.4em}\centering\vspace{-0.2em}%
      \includegraphics[width=2em,height=2em,keepaspectratio]{#1}%
    \end{minipage}\hspace{0.4em}%
    \begin{minipage}[t]{\dimexpr \linewidth - 2.8em\relax}
      \textbf{#2}\hfill{\small\color{mutedcolor}#3}\\[-0.1em]
      {\small\itshape\color{accentcolor}#4}\par\vspace{-0.2em}
      #5
    \end{minipage}%
  }\par
}

%% ---------- 项目卡片（v3.6: 微阴影背景）----------
% \projectCard{<标题>}{<时间>}{<一句话简介>}{<itemize 详细描述>}{<链接 footer>}
\newcommand{\projectCard}[5]{%
  \par\vspace{0.2em}\noindent
  %% 微阴影背景
  \begin{tikzpicture}
    \useasboundingbox (0,0) rectangle (\linewidth,0pt);
    \fill[cardcolor, rounded corners=2pt]
      (-0.3em,-0.2em) rectangle (\linewidth+0.1em,0.2em);
  \end{tikzpicture}%
  \vspace{-1.2em}%
  \makebox[0.45em][l]{\textcolor{themecolor}{\rule[-0.05em]{2pt}{0.95em}}}%
  \hspace{0.3em}\textbf{#1}\hfill{\small\color{mutedcolor}#2}\\[-0.1em]
  \hspace*{0.75em}{\small\itshape\color{accentcolor}#3}\par\vspace{-0.15em}
  \hspace*{0.75em}\begin{minipage}{\dimexpr\linewidth-0.75em\relax}
    #4
    \ifthenelse{\equal{#5}{}}{}{\par\vspace{-0.05em}{\footnotesize\color{mutedcolor}#5}}
  \end{minipage}\par
}

%% ---------- 开源项目 ----------
% \openSourceItem{<repo 名>}{<stars>}{<forks>}{<语言>}{<描述>}{<贡献 itemize>}
\NewDocumentCommand{\openSourceItem}{m m m m m m}{%
  \par\vspace{0.2em}\noindent
  {\bfseries\color{themecolor}\faGithub\ #1}\hfill
  {\footnotesize\color{accentcolor}\faStar\,#2\ \ \faCodeBranch\,#3\ \ \faCode\,#4}\\[-0.1em]
  {\small\itshape\color{mutedcolor}#5}\par\vspace{-0.2em}
  #6
}

%% ---------- 作品集 ----------
% \workItem[<thumb>]{<标题>}{<类型/平台>}{<链接>}{<描述>}
\NewDocumentCommand{\workItem}{O{} m m m m}{%
  \par\vspace{0.2em}\noindent
  \IfStrEq{#1}{}{%
    {\color{accentcolor}\faPaintBrush}\ %
  }{%
    \begin{minipage}[c]{2em}\centering
      \includegraphics[width=1.6em,height=1.6em,keepaspectratio]{#1}%
    \end{minipage}\hspace{0.2em}%
  }%
  \textbf{#2}\hfill{\small\color{mutedcolor}#3}\\[-0.1em]
  \hspace*{1.6em}{\small\color{accentcolor}\faExternalLink*\ \href{#4}{#4}}\quad{\small #5}\par
}

%% ---------- 论文发表（v3.6: 左侧装饰线）----------
\newcommand{\publicationItem}[4]{%
  \par\vspace{0.2em}\noindent
  \makebox[0.3em][l]{\textcolor{themecolor!30}{\rule[-0.1em]{1.5pt}{1.1em}}}%
  \hspace{0.3em}%
  \begin{minipage}{\dimexpr\linewidth-0.6em\relax}
    \textbf{#1}\\[-0.15em]
    {\small #2}\par\vspace{-0.1em}
    {\small\color{accentcolor}#3}\quad{\small #4}\par
  \end{minipage}%
}

%% ---------- 荣誉 / 奖项（v3.6: 左侧装饰线）----------
\newcommand{\awardItem}[3]{%
  \par\vspace{0.15em}\noindent
  \makebox[0.3em][l]{\textcolor{accentcolor!30}{\rule[-0.1em]{1.5pt}{1.1em}}}%
  \hspace{0.3em}%
  \begin{minipage}{\dimexpr\linewidth-0.6em\relax}
    {\color{accentcolor}\faTrophy}\ \textbf{#1}\hfill{\small\color{mutedcolor}#2}\\[-0.15em]
    \hspace*{1.1em}{\small #3}\par
  \end{minipage}%
}

%% ---------- 技能：单行 inline 风格 ----------
% \skillrow{<分类标题>}{<内容（可含 \skilltag）>}
\newcommand{\skillrow}[2]{%
  \par\noindent
  \makebox[5.6em][l]{\textbf{\small #1}}{\small #2}\par
}

%% ---------- 技能：紧凑进度条（v3.6: 渐变填充）----------
% \skillbar{<技能名>}{<level 0-10>}
\newcommand{\skillbar}[2]{%
  \par\noindent
  \makebox[8.5em][l]{\small\textbf{#1}}%
  \begin{tikzpicture}[baseline=-0.5ex]
    \fill[lightcolor,rounded corners=1pt] (0,0) rectangle (8,0.22);
    %% v3.6: 渐变填充进度条
    \shade[left color=themecolor, right color=accentcolor, rounded corners=1pt]
      (0,0) rectangle (#2/10*8,0.22);
  \end{tikzpicture}\hspace{0.4em}{\footnotesize\color{mutedcolor}#2/10}\par
}

%% ---------- 技能：圆点等级（5 级）----------
\newcommand{\skilldots}[2]{%
  \par\noindent
  \makebox[8.5em][l]{\small\textbf{#1}}%
  \foreach \x in {1,...,5}{%
    \ifnumgreater{\x}{#2}{\textcolor{lightcolor}{\footnotesize\faCircle}}{\textcolor{themecolor}{\footnotesize\faCircle}}\,%
  }\par
}

%% ---------- 技能：标签（v3.6: 微阴影）----------
\newcommand{\skilltag}[1]{%
  \tikz[baseline=(t.base)]
    \node[draw=themecolor!40, text=themecolor, rounded corners=2pt,
          inner xsep=4pt, inner ysep=1.2pt, font=\footnotesize,
          fill=lightcolor!50] (t) {#1};\hspace{0.5pt}%
}

\newcommand{\skilltagAccent}[1]{%
  \tikz[baseline=(t.base)]
    \node[fill=themecolor, text=white, rounded corners=2pt,
          inner xsep=4pt, inner ysep=1.4pt, font=\footnotesize\bfseries,
          drop shadow={shadow xshift=0.3pt, shadow yshift=-0.3pt,
                       fill=black!15, rounded corners=1pt}] (t) {#1};\hspace{0.5pt}%
}

%% ---------- 通用徽章（v3.6: 微阴影）----------
\newcommand{\badge}[2]{%
  \tikz[baseline=(b.base)]{%
    \node[fill=mutedcolor, text=white, rounded corners=2pt,
          inner xsep=3pt, inner ysep=1pt, font=\scriptsize\bfseries] (a) {#1};
    \node[fill=themecolor, text=white, rounded corners=2pt,
          right=1pt of a, inner xsep=3pt, inner ysep=1pt, font=\scriptsize\bfseries,
          drop shadow={shadow xshift=0.3pt, shadow yshift=-0.3pt,
                       fill=black!15, rounded corners=1pt}] (b) {#2};
  }\hspace{0.5pt}%
}

%% ---------- 页眉页脚（fancyhdr）----------
\AtBeginDocument{%
  \ifdef{\@name}{\let\rpName\@name}{\def\rpName{Resume}}%
  \ifdef{\@tagline}{\let\rpTag\@tagline}{\def\rpTag{}}%
  \ifdef{\@fileinfo}{\let\rpFileInfo\@fileinfo}{\def\rpFileInfo{}}%
  \ifdef{\@version}{\let\rpVer\@version}{\def\rpVer{}}%
}

% 页脚右侧内容（QR + version），避免 firstpage 与普通页重复
\newcommand{\rp@footerright}{%
  \ifdef{\@qrlink}{%
    \raisebox{-0.1em}{\qrcode[height=1.1em]{\@qrlink}}\hspace{0.3em}%
  }{}%
  \footnotesize\color{mutedcolor}\rpVer%
}

\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
%% v3.6: 页脚细线渐变效果
\renewcommand{\footrulewidth}{0pt}
\newcommand{\rp@footrule}{%
  \begin{tikzpicture}[remember picture, overlay]
    \shade[left color=themecolor!40, right color=themecolor!8]
      (current page.south west) ++(0.4cm, 0.55cm) rectangle ++(\paperwidth-0.8cm, 0.3pt);
  \end{tikzpicture}%
}

\if@rp@nofooter
  \pagestyle{empty}
\else
  \fancyhead[L]{\footnotesize\color{mutedcolor}\rpName}
  \fancyhead[R]{\footnotesize\color{mutedcolor}\rpTag}
  \fancyfoot[L]{\footnotesize\color{mutedcolor}\rpFileInfo}
  \fancyfoot[C]{\footnotesize\color{mutedcolor}\thepage\,/\,\pageref{LastPage}}
  \fancyfoot[R]{\rp@footerright}
  %% v3.6: 渐变页脚线
  \renewcommand{\footnoterule}{\rp@footrule}
\fi

% 首页：去掉 header（让 makeheader 占据），保留 footer
\fancypagestyle{firstpage}{%
  \fancyhf{}
  \renewcommand{\headrulewidth}{0pt}
  \renewcommand{\footrulewidth}{0pt}
  \if@rp@nofooter\else
    \fancyfoot[L]{\footnotesize\color{mutedcolor}\rpFileInfo}
    \fancyfoot[C]{\footnotesize\color{mutedcolor}\thepage\,/\,\pageref{LastPage}}
    \fancyfoot[R]{\rp@footerright}
  \fi
}
\AtBeginDocument{\thispagestyle{firstpage}}

%% ============================================================
%%  扩展原语（v3.2 → v3.6）
%% ============================================================

%% ---------- 双栏布局支持 ----------
% \begin{sidebar}{<width>} ... \end{sidebar}
% 在双栏布局的左侧 sidebar 中使用，自动应用更小的字号、紧凑列表、低饱和样式
\NewDocumentEnvironment{sidebar}{m}{%
  \begin{minipage}[t]{#1}
    \small\color{darkcolor}
    \setlength{\parskip}{0.3em}
}{%
  \end{minipage}%
}

% \sidesection{<title>}{<icon>} —— sidebar 内简化版章节标题
\newcommand{\sidesection}[2]{%
  \par\vspace{0.6em}\noindent
  {\footnotesize\bfseries\color{themecolor}\MakeUppercase{#1}}%
  \par\vspace{-0.4em}{\color{themecolor!50}\rule{\linewidth}{0.4pt}}%
  \par\vspace{0.1em}
}

% \mainpane{<width>} —— 双栏右侧主内容区入口
\newenvironment{mainpane}[1]{%
  \begin{minipage}[t]{#1}
}{%
  \end{minipage}%
}

%% ---------- 时间线条目 ----------
% \timelineEntry{<date>}{<title>}{<subtitle>}{<body>}
\newcommand{\timelineEntry}[4]{%
  \par\vspace{0.2em}\noindent
  \begin{minipage}[t]{4em}\raggedleft
    {\footnotesize\color{mutedcolor}#1}%
  \end{minipage}\hspace{0.4em}%
  \makebox[0.4em][l]{\textcolor{themecolor}{\rule[-0.05em]{1.5pt}{0.85em}}}%
  \hspace{0.3em}%
  \begin{minipage}[t]{\dimexpr\linewidth - 5em\relax}
    \textbf{#2}\ifthenelse{\equal{#3}{}}{}{ \textbullet{}\ {\small\itshape\color{accentcolor}#3}}%
    \par\vspace{-0.15em}{\small #4}%
  \end{minipage}\par
}

%% ---------- 求职信信封头 ----------
% \coverletterheader{<recipient name>}{<recipient title>}{<company>}{<address>}
\newcommand{\coverletterheader}[4]{%
  \par\vspace{0.6em}\noindent
  \begin{minipage}[t]{0.5\linewidth}
    {\large\bfseries\color{themecolor}\rpName}\\[-0.1em]
    {\small\color{mutedcolor}%
      \ifdef{\@email}{\faEnvelope\ \@email\\[-0.1em]}{}%
      \ifdef{\@phone}{\faPhone\ \@phone\\[-0.1em]}{}%
      \ifdef{\@location}{\faMapMarker*\ \@location}{}%
    }
  \end{minipage}\hfill
  \begin{minipage}[t]{0.45\linewidth}\raggedleft
    {\small\color{mutedcolor}\today}
  \end{minipage}
  \par\vspace{1.2em}\noindent
  \textbf{#1}\\
  \textit{#2}\\
  \textbf{#3}\\
  {\small\color{mutedcolor}#4}
  \par\vspace{0.8em}
  {\color{themecolor!60}\rule{\linewidth}{0.4pt}}
  \par\vspace{0.4em}
}

%% ---------- 单页极简横向条目（可用于荣誉一行展示）----------
% \inlineEntry{<icon>}{<标题>}{<时间或地点>}
\newcommand{\inlineEntry}[3]{%
  \par\vspace{0.05em}\noindent
  {\color{accentcolor}#1}\ \textbf{#2}\hfill{\small\color{mutedcolor}#3}\par
}

%% ---------- 引用 / 推荐人块 ----------
% \quoteBlock{<text>}{<source>}
\newcommand{\quoteBlock}[2]{%
  \par\vspace{0.4em}\noindent
  \begin{minipage}{\dimexpr\linewidth - 2em\relax}
    \hspace*{1em}\itshape\color{darkcolor}``#1''\par
    \hspace*{1em}\hfill\textemdash\ {\small\color{mutedcolor}#2}\hspace*{1em}
  \end{minipage}\par\vspace{0.4em}
}

%% ---------- 多列摆放（紧凑技能等）----------
% \begin{multiCol}{<n>}{<width>} item \\ item \\ ... \end{multiCol}
\NewDocumentEnvironment{multiCol}{m m}{%
  \par\vspace{0.1em}\noindent
  \begin{tabular}{*{#1}{p{#2}}}
}{%
  \end{tabular}\par
}

%% ---------- 页数溢出警告 ----------
\newcommand{\rp@maxpages}{999}
\newcommand{\setMaxPages}[1]{\def\rp@maxpages{#1}}
\AtEndDocument{%
  \ifnum\value{page}>\rp@maxpages
    \typeout{***********************************************}%
    \typeout{* WARNING: Resume exceeds \rp@maxpages\ page(s)!}%
    \typeout{* Current pages: \thepage}%
    \typeout{* Consider using [compact] option or trimming content.}%
    \typeout{***********************************************}%
  \fi
}

%% ---------- 条件渲染辅助 ----------
% \rpIfPageOne{<content>} — 仅在第 1 页渲染（如摘要只在首页显示）
\newcommand{\rpIfPageOne}[1]{%
  \ifnum\value{page}=1 #1\fi
}

%% ---------- 水平分割线（手动插入）----------
% \hdiv — 主题色半透明分割线
\newcommand{\hdiv}{%
  \par\vspace{0.3em}{\color{themecolor!40}\rule{\linewidth}{0.3pt}}\par\vspace{0.2em}%
}

%% ---------- 高亮文本 ----------
% \hltext{<text>} — 主题色高亮背景
\newcommand{\hltext}[1]{%
  \tikz[baseline=(t.base)]
    \node[fill=lightcolor,text=themecolor,rounded corners=2pt,
          inner xsep=4pt,inner ysep=1.2pt,font=\small\bfseries] (t) {#1};\hspace{0.5pt}%
}

%% ---------- 日期范围快捷 ----------
% \daterange{<start>}{<end>} — 格式化日期范围
\newcommand{\daterange}[2]{#1\,--\,#2}

%% ---------- 可折叠章节（配合 compact 模式自动折叠）----------
% \conditionalSection[<condition>]{<title>}{<icon>}{<content>}
% condition: show / hide / compact-only（仅在非 compact 时显示）
\NewDocumentCommand{\conditionalSection}{O{show} m m m}{%
  \IfStrEq{#1}{hide}{}{%
    \IfStrEq{#1}{compact-only}{%
      \if@rp@compact \sectionTitle{#2}{#3} #4 \fi
    }{%
      \sectionTitle{#2}{#3} #4%
    }%
  }%
}

%% ---------- 证书条目 ----------
% \certItem{<证书名>}{<颁发机构>}{<时间>}
\newcommand{\certItem}[3]{%
  \par\vspace{0.15em}\noindent
  {\color{accentcolor}\faCertificate}\ \textbf{#1}\hfill{\small\color{mutedcolor}#3}\\[-0.15em]
  \hspace*{1.4em}{\small\color{mutedcolor}#2}\par
}

%% ---------- 通用简历条目（无图标版）----------
% \resumeItem{<标题>}{<时间>}{<描述>}
\newcommand{\resumeItem}[3]{%
  \par\vspace{0.2em}\noindent
  \textbf{#1}\hfill{\small\color{mutedcolor}#2}\\[-0.1em]
  \hspace*{0em}{\small #3}\par
}

%% ---------- 最后更新日期（自动）----------
% \lastupdated — 在页脚或正文中插入 "Last updated: YYYY-MM-DD"
\newcommand{\lastupdated}{%
  \if@rp@zh 最后更新：\today\else Last updated: \today\fi%
}

%% ---------- Watermark（水印）----------
% \watermark{<text>} — 在每页中央显示浅色对角线水印
\newcommand{\watermark}[1]{%
  \AddToHook{shipout/background}{%
    \put(0.5\paperwidth,-0.5\paperheight){%
      \rotatebox{55}{%
        \textcolor{rulecolor!30}{\fontsize{48pt}{48pt}\selectfont\bfseries #1}%
      }%
    }%
  }%
}

\endinput
%% EOF
