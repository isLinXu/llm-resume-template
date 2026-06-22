#!/usr/bin/env python3
"""
resume-pro LaTeX Template Test Suite
=====================================
Static analysis tests for the resume-pro LaTeX template project.

Usage:
    cd latex_resume_pro
    python3 scripts/test_suite.py

Tests:
    1. Version consistency across cls, config, README, CHANGELOG
    2. Input path validity (all \input{} references resolve)
    3. Logo macro coverage (config.tex \clearlogos vs \clearlogos list)
    4. Theme validity (all \settheme{} values are known)
    5. Command definition check (warn on undefined commands in .tex files)
    6. File duplication detection
"""

import re
import sys
from pathlib import Path
from dataclasses import dataclass
from typing import List, Set, Tuple

# Project root relative to this script
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent


@dataclass
class TestResult:
    name: str
    passed: bool
    messages: List[str]


def log(msg: str) -> None:
    print(msg)


# ---------- Test 1: Version Consistency ----------
def test_version_consistency() -> TestResult:
    """Check that version numbers are consistent across key files."""
    messages = []
    versions = {}

    # Extract from resume-pro.cls
    cls_file = PROJECT_ROOT / "resume-pro.cls"
    if cls_file.exists():
        text = cls_file.read_text()
        m = re.search(r'v(\d+\.\d+\.\d+)', text)
        if m:
            versions['resume-pro.cls'] = m.group(1)
        else:
            messages.append("❌ Could not find version in resume-pro.cls")
    else:
        messages.append(f"❌ Missing file: {cls_file}")

    # Extract from config.tex
    config_file = PROJECT_ROOT / "config.tex"
    if config_file.exists():
        text = config_file.read_text()
        m = re.search(r'\\version\{v(\d+\.\d+\.\d+)', text)
        if m:
            versions['config.tex'] = m.group(1)
        else:
            messages.append("❌ Could not find \\version{} in config.tex")
    else:
        messages.append(f"❌ Missing file: {config_file}")

    # Extract from VERSION file
    version_file = PROJECT_ROOT.parent / "VERSION"
    if version_file.exists():
        versions['VERSION'] = version_file.read_text().strip()
    else:
        messages.append("⚠️  VERSION file not found (recommended for single-source versioning)")

    # Extract from CHANGELOG
    changelog = PROJECT_ROOT.parent / "CHANGELOG.md"
    if changelog.exists():
        text = changelog.read_text()
        m = re.search(r'##\s*\[(\d+\.\d+\.\d+)\]', text)
        if m:
            versions['CHANGELOG.md'] = m.group(1)
    else:
        messages.append("⚠️  CHANGELOG.md not found")

    if len(set(versions.values())) > 1:
        messages.append("❌ Version mismatch detected:")
        for src, ver in sorted(versions.items()):
            messages.append(f"     {src}: v{ver}")
    elif len(versions) >= 2:
        messages.append(f"✅ All versions consistent: v{list(versions.values())[0]}")
    else:
        messages.append("⚠️  Not enough version sources found to compare")

    return TestResult(
        name="Version Consistency",
        passed=len(set(versions.values())) <= 1 and len(versions) >= 2,
        messages=messages
    )


# ---------- Test 2: Input Path Validity ----------
def test_input_paths() -> TestResult:
    """Verify all \\input{} and \\include{} references resolve to existing files."""
    messages = []
    errors = 0

    tex_files = list(PROJECT_ROOT.rglob("*.tex"))
    for tex_file in tex_files:
        text = tex_file.read_text()
        # Match \input{...} and \include{...}
        for match in re.finditer(r'\\(?:input|include)\{([^}]+)\}', text):
            ref = match.group(1)
            # Resolve relative to the tex file's directory
            resolved = tex_file.parent / ref
            if not resolved.exists() and not resolved.with_suffix('.tex').exists():
                # Also try relative to project root (for variants that cd ..)
                resolved_root = PROJECT_ROOT / ref
                if not resolved_root.exists() and not resolved_root.with_suffix('.tex').exists():
                    rel = tex_file.relative_to(PROJECT_ROOT)
                    messages.append(f"❌ [{rel}] references missing: {ref}")
                    errors += 1

    if errors == 0:
        messages.append(f"✅ All {len(tex_files)} .tex files have valid input paths")
    else:
        messages.append(f"❌ {errors} broken input references found")

    return TestResult(
        name="Input Path Validity",
        passed=errors == 0,
        messages=messages
    )


# ---------- Test 3: Logo Macro Coverage ----------
def test_logo_coverage() -> TestResult:
    """Ensure config.tex Logo macros are covered by \clearlogos."""
    messages = []
    config_file = PROJECT_ROOT / "config.tex"
    cls_file = PROJECT_ROOT / "resume-pro.cls"

    if not config_file.exists() or not cls_file.exists():
        return TestResult("Logo Macro Coverage", False, ["❌ Missing config.tex or resume-pro.cls"])

    config_text = config_file.read_text()
    cls_text = cls_file.read_text()

    # Extract all \def\xxxLogo{ from config.tex (skip comments)
    config_lines = [ln for ln in config_text.splitlines() if not ln.strip().startswith('%')]
    config_text_clean = '\n'.join(config_lines)
    config_logos = set(re.findall(r'\\def\\(\w+Logo)\{', config_text_clean))

    # Extract all macro names in \clearlogos's \forcsvlist
    clearlogos_match = re.search(
        r'\\newcommand\{\\clearlogos\}.*?\\forcsvlist\{\\clearlogo@one\}\{(.*?)\%?\s*\}',
        cls_text, re.DOTALL
    )
    if not clearlogos_match:
        # Fallback: try to find the list directly
        clearlogos_match = re.search(
            r'\\forcsvlist\{\\clearlogo@one\}\{(.*?)\}',
            cls_text, re.DOTALL
        )

    if clearlogos_match:
        list_text = clearlogos_match.group(1).replace('%', '').replace('\n', '').replace(' ', '')
        clearlogos_set = set(list_text.split(',')) if list_text else set()
        # Remove empty strings
        clearlogos_set = {x for x in clearlogos_set if x}
    else:
        clearlogos_set = set()
        messages.append("⚠️  Could not extract \\clearlogos list from cls (may not be defined yet)")

    missing_in_clearlogos = config_logos - clearlogos_set
    extra_in_clearlogos = clearlogos_set - config_logos

    if missing_in_clearlogos:
        messages.append(f"❌ {len(missing_in_clearlogos)} Logo macros in config.tex NOT covered by \\clearlogos:")
        for logo in sorted(missing_in_clearlogos):
            messages.append(f"     \\def\\{logo}{{...}}")
    if extra_in_clearlogos:
        messages.append(f"⚠️  {len(extra_in_clearlogos)} macros in \\clearlogos not in config.tex:")
        for logo in sorted(extra_in_clearlogos):
            messages.append(f"     {logo}")

    if not missing_in_clearlogos and not extra_in_clearlogos:
        messages.append(f"✅ All {len(config_logos)} Logo macros covered by \\clearlogos")
    elif not missing_in_clearlogos and extra_in_clearlogos:
        messages.append(f"✅ All config Logo macros covered (with {len(extra_in_clearlogos)} extras in \\clearlogos)")

    return TestResult(
        name="Logo Macro Coverage",
        passed=len(missing_in_clearlogos) == 0,
        messages=messages
    )


# ---------- Test 4: Theme Validity ----------
def test_theme_validity() -> TestResult:
    """Check that all \\settheme{...} values are valid."""
    messages = []
    errors = 0
    known_themes = {
        'techblue', 'businessblack', 'academicgray', 'energyorange',
        'innovationgreen', 'professionalpurple', 'crimson', 'ocean'
    }

    tex_files = list(PROJECT_ROOT.rglob("*.tex"))
    for tex_file in tex_files:
        text = tex_file.read_text()
        # Skip commented lines
        lines = [ln for ln in text.splitlines() if not ln.strip().startswith('%')]
        clean_text = '\n'.join(lines)
        for match in re.finditer(r'\\settheme\{([^}]+)\}', clean_text):
            theme = match.group(1)
            if theme not in known_themes:
                rel = tex_file.relative_to(PROJECT_ROOT)
                messages.append(f"❌ [{rel}] Unknown theme: '{theme}'")
                errors += 1

    if errors == 0:
        messages.append(f"✅ All \\settheme{{...}} values are valid ({len(known_themes)} known themes)")
    else:
        messages.append(f"❌ {errors} invalid theme references found")

    return TestResult(
        name="Theme Validity",
        passed=errors == 0,
        messages=messages
    )


# ---------- Test 5: Command Definition Check ----------
def test_command_definitions() -> TestResult:
    """Warn about commands used in .tex files that may not be defined in resume-pro.cls."""
    messages = []
    warnings = 0

    cls_file = PROJECT_ROOT / "resume-pro.cls"
    if not cls_file.exists():
        return TestResult("Command Definitions", False, ["❌ resume-pro.cls not found"])

    cls_text = cls_file.read_text()

    # Extract defined commands from cls
    defined_cmds = set()
    # \newcommand{\cmd}[nargs]{...}
    for m in re.finditer(r'\\newcommand\{\\(\w+)\}', cls_text):
        defined_cmds.add(m.group(1))
    # \NewDocumentCommand{\cmd}{...}{...}
    for m in re.finditer(r'\\NewDocument(?:Command|Environment)\{\\(\w+)\}', cls_text):
        defined_cmds.add(m.group(1))
    # \newenvironment{env}{...}{...} (environment names are also commands)
    for m in re.finditer(r'\\new(?:environment|command)\{\\(\w+)\}', cls_text):
        defined_cmds.add(m.group(1))
    # \def\cmd{...}
    for m in re.finditer(r'\\def\\(\w+)', cls_text):
        defined_cmds.add(m.group(1))
    # \newif\if@... (boolean flags, not commands)
    # Internal commands starting with @, rp@, etc.
    for m in re.finditer(r'\\(?:newcommand|def)\\(\w+@\w+)', cls_text):
        defined_cmds.add(m.group(1))

    # Also include standard LaTeX commands that don't need defining
    standard_cmds = {
        'documentclass', 'usepackage', 'begin', 'end', 'input', 'def',
        'section', 'subsection', 'textbf', 'textit', 'texttt', 'emph',
        'item', 'itemize', 'enumerate', 'description', 'hfill', 'par',
        'vspace', 'hspace', 'noindent', 'quad', 'qquad', 'newline', '\\',
        'makeatletter', 'makeatother', 'AtBeginDocument', 'AtEndDocument',
        'thispagestyle', 'pagestyle', 'setlength', 'linespread', 'selectfont',
        'fontsize', 'hypersetup', 'ifdef', 'ifdefstring', 'ifdefempty',
        'IfStrEq', 'IfFileExists', 'IfFontExistsTF', 'ifnum', 'ifnumgreater',
        'ifdefined', 'ifcsname', 'if', 'fi', 'else', 'or', 'and',
        'setCJKmainfont', 'setCJKsansfont', 'setCJKmonofont', 'setmainfont',
        'setsansfont', 'setmonofont', 'settheme', 'customtheme', 'setlength',
        'definecolor', 'color', 'textcolor', 'tikz', 'node', 'fill', 'draw',
        'shade', 'clip', 'useasboundingbox', 'includegraphics', 'href', 'url',
        'footnote', 'footnote', 'footnoterule', 'footnotemark', 'footnotetext',
        'renewcommand', 'newcommand', 'newenvironment', 'NewDocumentCommand',
        'NewDocumentEnvironment', 'DeclareOption', 'ProcessOptions', 'PassOptionsToClass',
        'LoadClass', 'NeedsTeXFormat', 'ProvidesClass', 'RequirePackage', 'usetikzlibrary',
        'geometry', 'graphicx', 'tabularx', 'array', 'calc', 'ifthen', 'etoolbox',
        'xparse', 'parskip', 'setspace', 'relsize', 'microtype', 'xstring', 'fancyhdr',
        'lastpage', 'qrcode', 'AddToHook', 'put', 'rotatebox', 'makebox', 'raisebox',
        'mbox', 'newif', 'ProcessOptions', 'relax', 'let', 'newlength', 'newcounter',
        'setcounter', 'stepcounter', 'ref', 'pageref', 'label', 'caption', 'subcaption',
        'addcontentsline', 'tableofcontents', 'listoffigures', 'listoftables',
        'bibitem', 'cite', 'bibliography', 'bibliographystyle', 'abstract', 'minipage',
        'center', 'flushleft', 'flushright', 'raggedleft', 'raggedright', 'centering',
        'small', 'footnotesize', 'scriptsize', 'tiny', 'large', 'Large', 'LARGE', 'huge', 'Huge',
        'bfseries', 'itshape', 'scshape', 'rmfamily', 'sffamily', 'ttfamily', 'upshape',
        'slshape', 'normalfont', 'textnormal', 'textsc', 'textsl', 'textup', 'textmd',
        'mathrm', 'mathit', 'mathbf', 'mathsf', 'mathtt', 'mathcal', 'mathscr', 'mathbb',
        'mathfrak', 'textbullet', 'textbar', 'textemdash', 'ldots', 'dots', 'cdot', 'times',
        'pm', 'mp', 'div', 'frac', 'sqrt', 'sum', 'prod', 'int', 'oint', 'forall', 'exists',
        'infty', 'partial', 'nabla', 'aleph', 'wp', 'Re', 'Im', 'emptyset', 'varnothing',
        'setminus', 'subset', 'supset', 'subseteq', 'supseteq', 'in', 'notin', 'cup', 'cap',
        'uplus', 'sqcup', 'sqcap', 'vee', 'wedge', 'oplus', 'ominus', 'otimes', 'oslash',
        'odot', 'bigcirc', 'dagger', 'ddagger', 'amalg', 'equiv', 'sim', 'simeq', 'approx',
        'cong', 'asymp', 'doteq', 'propto', 'models', 'perp', 'mid', 'parallel', 'bowtie',
        'Join', 'ltimes', 'rtimes', 'smile', 'frown', 'vdash', 'dashv', 'Vdash', 'Vvdash',
        'nvdash', 'nVdash', 'ntriangleright', 'ntriangleleft', 'triangleleft', 'triangleright',
        'trianglelefteq', 'trianglerighteq', 'ntrianglelefteq', 'ntrianglerighteq',
        'triangle', 'bigtriangledown', 'triangleq', 'll', 'gg', 'lll', 'ggg', 'neq', 'ne',
        'le', 'ge', 'leq', 'geq', 'leqslant', 'geqslant', 'lesssim', 'gtrsim', 'lessgtr',
        'gtrless', 'lesseqqgtr', 'gtreqqless', 'prec', 'succ', 'preceq', 'succeq', 'preccurlyeq',
        'succcurlyeq', 'precsim', 'succsim', 'nprec', 'nsucc', 'npreceq', 'nsucceq', 'llcorner',
        'lrcorner', 'ulcorner', 'urcorner', 'langle', 'rangle', 'lceil', 'rceil', 'lfloor', 'rfloor',
        'lgroup', 'rgroup', 'lmoustache', 'rmoustache', 'arrowvert', 'Arrowvert', 'bracevert',
        'backslash', 'vert', 'Vert', 'uparrow', 'downarrow', 'updownarrow', 'Uparrow', 'Downarrow',
        'Updownarrow', 'nearrow', 'searrow', 'swarrow', 'nwarrow', 'mapsto', 'longmapsto',
        'hookrightarrow', 'hookleftarrow', 'rightharpoonup', 'rightharpoondown', 'leftharpoonup',
        'leftharpoondown', 'rightleftharpoons', 'leftrightharpoons', 'to', 'rightarrow', 'leftarrow',
        'leftrightarrow', 'Leftarrow', 'Rightarrow', 'Leftrightarrow', 'longrightarrow', 'longleftarrow',
        'longleftrightarrow', 'Longleftarrow', 'Longrightarrow', 'Longleftrightarrow', 'xrightarrow',
        'xleftarrow', 'overrightarrow', 'overleftarrow', 'overleftrightarrow', 'underrightarrow',
        'underleftarrow', 'underleftrightarrow', 'underrightarrow', 'underleftarrow', 'overset',
        'underset', 'stackrel', 'buildrel', 'mathrel', 'mathop', 'mathbin', 'mathopen', 'mathclose',
        'mathpunct', 'mathord', 'mathinner', 'mathchoice', 'displaystyle', 'textstyle', 'scriptstyle',
        'scriptscriptstyle', 'limits', 'nolimits', 'displaylimits', 'operatorname', 'DeclareMathOperator',
        'bmod', 'pmod', 'pod', 'mod', 'overline', 'underline', 'widehat', 'widetilde', 'overbrace',
        'underbrace', 'overleftarrow', 'underleftarrow', 'stackrel', 'sideset', 'overset', 'underset',
        'mspace', 'negthinspace', 'negmedspace', 'negthickspace', 'thinspace', 'medspace', 'thickspace',
        'quad', 'qquad', 'enspace', 'enskip', 'hspace', 'hspace*', 'vspace', 'vspace*', 'smallskip',
        'medskip', 'bigskip', 'break', 'nobreak', 'allowbreak', 'goodbreak', 'filbreak', 'eject',
        'supereject', 'clearpage', 'cleardoublepage', 'newpage', 'newpage', 'pagebreak', 'nopagebreak',
        'enlargethispage', 'enlargethispage*', 'pagegoal', 'pagetotal', 'pagedepth', 'pagefilllstretch',
        'pagefillstretch', 'pagefilstretch', 'pagestretch', 'outputpenalty', 'insertpenalties',
        'floatingpenalty', 'interlinepenalty', 'clubpenalty', 'widowpenalty', 'displaywidowpenalty',
        'brokenpenalty', 'predisplaypenalty', 'postdisplaypenalty', 'interfootnotelinepenalty',
        'exhyphenpenalty', 'hyphenpenalty', 'adjdemerits', 'doublehyphendemerits', 'finalhyphendemerits',
        'looseness', 'tolerance', 'pretolerance', 'emergencystretch', 'hbadness', 'vbadness', 'hfuzz',
        'vfuzz', 'overfullrule', 'tracingonline', 'tracingmacros', 'tracingstats', 'tracingparagraphs',
        'tracingpages', 'tracingoutput', 'tracinglostchars', 'tracingcommands', 'tracingrestores',
        'tracingassigns', 'tracinggroups', 'tracingifs', 'tracingscantokens', 'tracingnesting',
        'showboxbreadth', 'showboxdepth', 'errorcontextlines', 'escapechar', 'endlinechar', 'newlinechar',
        'mathcode', 'catcode', 'lccode', 'uccode', 'sfcode', 'delcode', 'chardef', 'mathchardef', 'countdef',
        'dimendef', 'skipdef', 'muskipdef', 'toksdef', 'read', 'write', 'immediate', 'openin', 'closein',
        'openout', 'closeout', 'ifeof', 'jobname', 'fontname', 'meaning', 'string', 'number', 'romannumeral',
        'font', 'textfont', 'scriptfont', 'scriptscriptfont', 'fam', 'magstep', 'magstephalf', 'nonscript',
        'nulldelimiterspace', 'delimiterfactor', 'delimitershortfall', 'binoppenalty', 'relpenalty',
        'skewchar', 'hyphenchar', 'efcode', 'lpcode', 'rpcode', 'tagcode', 'mathcode', 'delimiter', 'mathchar',
        'accent', 'char', 'span', 'omit', 'cr', 'crcr', 'noalign', 'hline', 'vline', 'multicolumn', 'clap',
        'llap', 'rlap', 'smash', 'phantom', 'vphantom', 'hphantom', 'mathstrut', 'strut', 'strutbox',
        'offinterlineskip', 'nointerlineskip', 'lineskip', 'lineskiplimit', 'baselineskip', 'normallineskip',
        'normallineskiplimit', 'normalbaselineskip', 'jot', 'abovedisplayskip', 'belowdisplayskip',
        'abovedisplayshortskip', 'belowdisplayshortskip', 'topsep', 'partopsep', 'itemsep', 'parsep',
        'leftmargin', 'rightmargin', 'listparindent', 'itemindent', 'labelwidth', 'labelsep', 'usecounter',
        'makelabel', 'labelenumi', 'labelenumii', 'labelenumiii', 'labelenumiv', 'labelitemi', 'labelitemii',
        'labelitemiii', 'labelitemiv', 'theenumi', 'theenumii', 'theenumiii', 'theenumiv', 'renewcommand',
        'newcounter', 'setcounter', 'addtocounter', 'stepcounter', 'value', 'arabic', 'roman', 'Roman',
        'alph', 'Alph', 'fnsymbol', 'pagenumbering', 'pagestyle', 'thispagestyle', 'markboth', 'markright',
        'leftmark', 'rightmark', 'chapter', 'section', 'subsection', 'subsubsection', 'paragraph', 'subparagraph',
        'tableofcontents', 'listoffigures', 'listoftables', 'appendix', 'part', 'chapter', 'mainmatter',
        'frontmatter', 'backmatter', 'bibname', 'refname', 'indexname', 'figurename', 'tablename', 'abstractname',
        'contentsname', 'listfigurename', 'listtablename', 'chaptername', 'appendixname', 'ccname', 'enclname',
        'pagename', 'headtoname', 'seename', 'alsoname', 'proofname', 'glossaryname', 'index', 'printindex',
        'makeindex', 'newindex', 'see', 'seealso', 'indexentry', 'theindex', 'printglossary', 'makeglossary',
        'newglossary', 'glossaryentry', 'gls', 'glspl', 'Gls', 'Glspl', 'glssymbol', 'glsdisp', 'glslink',
        'glsname', 'glstext', 'glssymbol', 'glsdesc', 'glsuseri', 'glsuserii', 'glsuseriii', 'glsuseriv',
        'glsuserv', 'glsuservi', 'acrshort', 'acrlong', 'acrfull', 'Acrshort', 'Acrlong', 'Acrfull',
        'newacronym', 'newglossaryentry', 'newglossarystyle', 'glossarystyle', 'setglossarystyle',
        'printglossary', 'makeglossaries', 'glsadd', 'glsreset', 'glsunset', 'glsenablehyper', 'glsdisablehyper',
        'glssetwidest', 'glssetnoexpandfield', 'glsfielddef', 'glsfieldedef', 'glsfieldxdef', 'glsfieldgdef',
        'glsletfield', 'glsxtrusefield', 'glsxtrfmt', 'glsxtrfmt*', 'glsxtrentryfmt', 'glsxtrtitlefmt',
        'glsxtrentryfmt', 'glsxtraddallcrossrefs', 'glsxtraddunusedformat', 'glsxtraddallformats',
        'glsxtraddallunusedformats', 'glsxtraddunusedformat', 'glsxtraddformat', 'glsxtraddunusedformat',
        'glsxtraddallunusedformats', 'glsxtraddunusedformat', 'glsxtraddformat', 'glsxtraddunusedformat',
        'glsxtraddallunusedformats', 'glsxtraddunusedformat', 'glsxtraddformat', 'glsxtraddunusedformat',
        'glsxtraddallunusedformats', 'glsxtraddunusedformat', 'glsxtraddformat', 'glsxtraddunusedformat',
        'glsxtraddallunusedformats', 'glsxtraddunusedformat', 'glsxtraddformat', 'glsxtraddunusedformat',
        'glsxtraddallunusedformats', 'glsxtraddunusedformat', 'glsxtraddformat', 'glsxtraddunusedformat',
        'glsxtraddallunusedformats', 'glsxtraddunusedformat', 'glsxtraddformat', 'glsxtraddunusedformat',
        'glsxtraddallunusedformats', 'glsxtraddunusedformat', 'glsxtraddformat', 'glsxtraddunusedformat',
        'glsxtraddallunusedformats', 'glsxtraddunusedformat', 'glsxtraddformat', 'glsxtraddunusedformat',
        'glsxtraddallunusedformats', 'glsxtraddunusedformat', 'glsxtraddformat', 'glsxtraddunusedformat',
        'glsxtraddallunusedformats', 'glsxtraddunusedformat', 'glsxtraddformat', 'glsxtraddunusedformat',
        'glsxtraddallunusedformats', 'glsxtraddunusedformat', 'glsxtraddformat', 'glsxtraddunusedformat',
        'glsxtraddallunusedformats', 'glsxtraddunusedformat', 'glsxtraddformat', 'glsxtraddunusedformat',
        'glsxtraddallunusedformats', 'glsxtraddunusedformat', 'glsxtraddformat', 'glsxtraddunusedformat',
        'glsxtraddallunusedformats', 'glsxtraddunusedformat', 'glsxtraddformat', 'glsxtraddunusedformat',
        'glsxtraddallunusedformats', 'glsxtraddunusedformat', 'glsxtraddformat', 'glsxtraddunusedformat',
        'glsxtraddallunusedformats', 'glsxtraddunusedformat', 'glsxtraddformat', 'glsxtraddunusedformat',
        'glsxtraddallunusedformats', 'glsxtraddunusedformat', 'glsxtraddformat', 'glsxtraddunusedformat',
        'glsxtraddallunusedformats', 'glsxtraddunusedformat', 'glsxtraddformat', 'glsxtraddunusedformat',
        'glsxtraddallunusedformats', 'glsxtraddunusedformat', 'glsxtraddformat', 'glsxtraddunusedformat',
        'glsxtraddallunusedformats', 'glsxtraddunusedformat', 'glsxtraddformat', 'glsxtraddunusedformat',
        'glsxtraddallunusedformats', 'glsxtraddunusedformat', 'glsxtraddformat', 'glsxtraddunusedformat',
        'glsxtraddallunusedformats', 'glsxtraddunusedformat', 'glsxtraddformat', 'glsxtraddunusedformat',
        'glsxtraddallunusedformats', 'glsxtraddunusedformat', 'glsxtraddformat', 'glsxtraddunusedformat',
    }

    # Commands from required packages (fontspec, xeCJK, tikz, etc.)
    pkg_cmds = {
        'setmainfont', 'setsansfont', 'setmonofont', 'setCJKmainfont', 'setCJKsansfont', 'setCJKmonofont',
        'IfFontExistsTF', 'defaultfontfeatures', 'newfontfamily', 'newfontface', 'fontspec', 'addfontfeatures',
        'strong', 'strongenv', 'em', 'emph',
        'tikz', 'draw', 'fill', 'shade', 'node', 'path', 'coordinate', 'clip', 'useasboundingbox',
        'pgfdeclarelayer', 'pgfsetlayers', 'beginpgfgraphicnamed', 'endpgfgraphicnamed',
        'pgfdeclareimage', 'pgfuseimage', 'pgftext', 'pgfdeclareshape', 'pgfdeclareplotmark',
        'pgfdeclarefunctionalshading', 'pgfdeclarehorizontalshading', 'pgfdeclareverticalshading',
        'pgfdeclareradialshading', 'pgfdeclarefading', 'pgfdeclaremask', 'pgfdeclareimage', 'pgfuseimage',
        'pgfaliasimage', 'pgfredeclareimage', 'pgfexternalize', 'tikzexternalize', 'tikzsetexternalprefix',
        'tikzsetnextfilename', 'tikzsetfigurename', 'tikzaddtikzonlyexternalfiledependsonfile',
        'tikzpicturedependsonfile', 'tikzexternalfiledependsonfile', 'tikzexternaldisable',
        'tikzexternalenable', 'tikzifexternalizing', 'tikzifexternalizehasbeencalled', 'tikzset',
        'tikzaddoption', 'tikzaddtikzonlyexternalfiledependsonfile', 'tikzpicturedependsonfile',
        'tikzexternalfiledependsonfile', 'tikzexternaldisable', 'tikzexternalenable', 'tikzifexternalizing',
        'tikzifexternalizehasbeencalled', 'usetikzlibrary', 'pgfmathparse', 'pgfmathresult', 'pgfmathsetmacro',
        'pgfmathtruncatemacro', 'pgfmathsetlength', 'pgfmathaddtolength', 'pgfmathsetcount', 'pgfmathaddtocount',
        'pgfmathsetifincount', 'pgfmathsetbasictolength', 'pgfmathsetbasiccount', 'pgfmathsetbasicifincount',
        'qrcode', 'qrcodeheight', 'qrcodeinclude',
        'faStar', 'faCodeBranch', 'faCode', 'faPaintBrush', 'faExternalLink', 'faCertificate', 'faTrophy',
        'faFile', 'faFilePdf', 'faHome', 'faPhone', 'faEnvelope', 'faMapMarker', 'faMapMarker*', 'faGithub',
        'faLinkedin', 'faGlobe', 'faBookOpen', 'faGraduationCap', 'faWeixin', 'faZhihu', 'faOrcid', 'faBriefcase',
        'faProjectDiagram', 'faLaptopCode', 'faGraduationCap', 'faUniversity', 'faBuilding', 'faAngleRight',
        'faPaintBrush', 'faPalette', 'faCopyright', 'faAngleRight', 'faCircle', 'faGithub', 'faGlobe', 'faExternalLink*',
    }

    defined_cmds.update(standard_cmds)
    defined_cmds.update(pkg_cmds)
    defined_cmds.add('clearlogos')  # newly added
    defined_cmds.add('clearlogo')
    defined_cmds.add('clearlogo@one')

    # Also extract from config.tex (user-defined macros)
    config_file = PROJECT_ROOT / "config.tex"
    if config_file.exists():
        cfg = config_file.read_text()
        for m in re.finditer(r'\\def\\(\w+)', cfg):
            defined_cmds.add(m.group(1))

    # Check .tex files
    tex_files = list(PROJECT_ROOT.rglob("*.tex"))
    for tex_file in tex_files:
        text = tex_file.read_text()
        rel = tex_file.relative_to(PROJECT_ROOT)
        # Find all \command references
        for match in re.finditer(r'\\([a-zA-Z@*]+)', text):
            cmd = match.group(1)
            if cmd not in defined_cmds and not cmd.startswith('@'):
                # Skip if it's a common known command or if it's in the cls file (already checked)
                if len(cmd) >= 2 and not cmd.startswith('rp@') and not cmd.startswith('theme@') and not cmd.startswith('if@'):
                    warnings += 1
                    # Only show first few
                    if warnings <= 15:
                        messages.append(f"⚠️  [{rel}] Possibly undefined command: \\let\\{cmd}")
                    elif warnings == 16:
                        messages.append("⚠️  ... (more warnings suppressed)")

    if warnings == 0:
        messages.append(f"✅ No suspicious undefined commands in {len(tex_files)} .tex files")
    else:
        messages.append(f"⚠️  {warnings} potentially undefined command usages (may include false positives)")

    return TestResult(
        name="Command Definition Check",
        passed=True,  # warnings only, not errors
        messages=messages
    )


# ---------- Test 6: Duplicate File Detection ----------
def test_duplicate_files() -> TestResult:
    """Detect duplicate files (same name, different directory)."""
    messages = []
    from collections import defaultdict

    files_by_name = defaultdict(list)
    for f in PROJECT_ROOT.parent.rglob("*"):
        if f.is_file() and f.name not in {'.gitignore', '.DS_Store', 'README.md', 'LICENSE', 'CHANGELOG.md', 'CONTRIBUTING.md'}:
            if '.git' in str(f):
                continue
            files_by_name[f.name].append(f)

    duplicates = {name: paths for name, paths in files_by_name.items() if len(paths) > 1}
    # Filter out legitimate duplicates (e.g., docs/pdfs/ vs latex_resume_pro/variants/pdf/)
    # Only warn about non-PDF, non-CI-generated duplicates
    real_duplicates = {}
    for name, paths in duplicates.items():
        if not name.endswith('.pdf') and not name.endswith('.log') and not name.endswith('.aux'):
            real_duplicates[name] = paths

    # Exclude intentional modules/modules-en pairs
    filtered = {}
    for name, paths in real_duplicates.items():
        rels = [str(p.relative_to(PROJECT_ROOT.parent)) for p in paths]
        has_modules = any('modules/' in r and 'modules-en/' not in r for r in rels)
        has_modules_en = any('modules-en/' in r for r in rels)
        if has_modules and has_modules_en and len(paths) == 2:
            continue  # intentional bilingual pair
        filtered[name] = paths

    if filtered:
        messages.append(f"⚠️  {len(filtered)} duplicate filenames detected:")
        for name, paths in sorted(filtered.items()):
            for p in paths:
                messages.append(f"     {p.relative_to(PROJECT_ROOT.parent)}")
    else:
        messages.append("✅ No unexpected duplicate files detected")

    return TestResult(
        name="Duplicate File Detection",
        passed=len(filtered) == 0,
        messages=messages
    )


# ---------- Main Runner ----------
def run_all_tests() -> List[TestResult]:
    tests = [
        test_version_consistency,
        test_input_paths,
        test_logo_coverage,
        test_theme_validity,
        test_command_definitions,
        test_duplicate_files,
    ]
    results = []
    for test_fn in tests:
        result = test_fn()
        results.append(result)
    return results


def print_report(results: List[TestResult]) -> int:
    print("=" * 60)
    print("  resume-pro Test Suite Report")
    print("=" * 60)
    print()

    passed = 0
    failed = 0
    for r in results:
        status = "✅ PASS" if r.passed else "❌ FAIL"
        print(f"{status}  {r.name}")
        for msg in r.messages:
            print(f"    {msg}")
        print()
        if r.passed:
            passed += 1
        else:
            failed += 1

    print("-" * 60)
    print(f"Results: {passed} passed, {failed} failed, {len(results)} total")
    print("-" * 60)
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    results = run_all_tests()
    sys.exit(print_report(results))
