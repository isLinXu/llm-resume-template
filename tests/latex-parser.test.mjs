import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);
const LP = require('../docs/latex-parser.js');
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const read = relative => fs.readFileSync(path.join(root, relative), 'utf8');

test('config commands retain nested LaTeX and complete keyword values', () => {
  const source = read('latex_resume_pro/config.tex');
  assert.equal(LP.getArgument(source, 'name'), 'Hertz');
  assert.equal(
    LP.getArgument(source, 'keywords'),
    String.raw`LLM \textbullet{} PyTorch \textbullet{} DeepSpeed \textbullet{} RAG \textbullet{} Agent \textbullet{} 模型压缩`,
  );
  assert.equal(LP.getArgument(source, 'website'), 'https://hertz.dev');
});

test('real education, experience, project, and publication modules parse completely', () => {
  const education = read('latex_resume_pro/modules/education.tex');
  const educationItems = LP.findCommands(education, 'educationItem');
  assert.equal(educationItems.length, 2);
  assert.equal(educationItems[0].optional[0].value, String.raw`\tsinghuaLogo`);
  assert.match(educationItems[0].args[0].value, /清华大学/);
  assert.equal(educationItems[0].args.length, 4);

  const experience = read('latex_resume_pro/modules/experience.tex');
  const experienceItems = LP.findCommands(experience, 'experienceItem');
  assert.equal(experienceItems.length, 3);
  assert.match(experienceItems[0].args[3].value, /HumanEval\/MATH\/GSM8K/);
  assert.ok(LP.findEnvironment(experienceItems[0].args[3].value, 'itemize'));

  const projects = read('latex_resume_pro/modules/projects.tex');
  const projectCards = LP.findCommands(projects, 'projectCard');
  assert.equal(projectCards.length, 3);
  assert.equal(projectCards[0].args.length, 5);
  assert.match(projectCards[0].args[0].value, /SelfRAG-Agent/);
  assert.match(projectCards[2].args[4].value, /hertz\/fastinfer/);

  const publications = read('latex_resume_pro/modules/publications.tex');
  const publicationItems = LP.findCommands(publications, 'publicationItem');
  assert.equal(publicationItems.length, 3);
  assert.equal(publicationItems[0].args[1].value, String.raw`\textbf{Hertz}, Li Si, Wang Wu`);
  assert.match(publicationItems[0].args[3].value, /\\href\{https:\/\/arxiv\.org\/abs\/2410\.xxxxx\}\{\\faFilePdf\\ Paper\}/);
  assert.match(publicationItems[0].args[3].value, /\\href\{https:\/\/github\.com\/hertz\/hkd-llm\}\{\\faGithub\\ Code\}/);
});

test('replacing one argument preserves all surrounding content and literal $&', () => {
  const source = read('latex_resume_pro/config.tex');
  const keywords = LP.findCommand(source, 'keywords');
  const replacement = String.raw`LLM $& \textbf{Agent}`;
  const updated = LP.replaceArgument(source, keywords, 0, replacement);
  assert.equal(LP.getArgument(updated, 'keywords'), replacement);
  assert.equal(LP.getArgument(updated, 'name'), 'Hertz');
  assert.equal(LP.getArgument(updated, 'email'), 'adong@example.com');
  const argument = keywords.args[0];
  assert.equal(updated.slice(0, argument.contentStart), source.slice(0, argument.contentStart));
  assert.equal(updated.slice(argument.contentStart + replacement.length), source.slice(argument.contentEnd));
});

test('commented commands are skipped unless explicitly restored', () => {
  const source = '% \\name{Old}\n\\name{Active}\n';
  assert.equal(LP.findCommands(source, 'name').length, 1);
  assert.equal(LP.getArgument(source, 'name'), 'Active');
  assert.equal(LP.findCommands(source, 'name', { allowCommented: true }).length, 2);
  assert.equal(LP.upsertCommand('% \\name{Old}\n', 'name', 'Restored'), '\\name{Restored}\n');
});

test('environment scanning handles nesting and item text', () => {
  const source = String.raw`\begin{itemize}
  \item outer
  \begin{itemize}
    \item inner
  \end{itemize}
\end{itemize}`;
  const environment = LP.findEnvironment(source, 'itemize');
  assert.equal(environment.end, source.length);
  assert.match(LP.itemizeLines(environment), /inner/);
  assert.equal(LP.makeItemize(' first \nsecond'), '\\begin{itemize}\n  \\item first\n  \\item second\n\\end{itemize}');
});

test('range and command removal do not damage the following command', () => {
  const source = '\\name{Hertz}\n\\email{adong@example.com}\n';
  const command = LP.findCommand(source, 'name');
  assert.equal(LP.removeCommand(source, command), '\\email{adong@example.com}\n');
  assert.equal(LP.removeRange('abcdef', 1, 3), 'adef');
});

test('unbalanced commands are rejected without partial matches', () => {
  assert.equal(LP.findCommand('\\name{broken', 'name'), null);
  assert.equal(LP.findCommand(String.raw`\\name{Escaped}`, 'name'), null);
});

test('editor default projects and publications stay aligned with real modules', () => {
  const html = read('docs/editor.html');
  const editorDefault = name => {
    const match = html.match(new RegExp(`DF\\['${name}\\.tex'\\]=\`([\\s\\S]*?)\`;`));
    assert.ok(match, `Missing editor default for ${name}.tex`);
    return Function(`return \`${match[1]}\`;`)();
  };
  for (const [name, command] of [['projects', 'projectCard'], ['publications', 'publicationItem']]) {
    assert.equal(
      LP.findCommands(editorDefault(name), command).length,
      LP.findCommands(read(`latex_resume_pro/modules/${name}.tex`), command).length,
    );
  }
  assert.equal(
    LP.findCommands(editorDefault('publications'), 'awardItem').length,
    LP.findCommands(read('latex_resume_pro/modules/publications.tex'), 'awardItem').length,
  );
});
