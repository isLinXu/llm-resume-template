/*
 * Resume Pro — small, dependency-free LaTeX command scanner.
 * Handles nested braces/brackets, escaped characters and commented commands.
 * Works in the browser (window.ResumeLatex) and in Node.js tests.
 */
(function (root, factory) {
  const api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  if (root) root.ResumeLatex = api;
})(typeof globalThis !== 'undefined' ? globalThis : this, function () {
  'use strict';

  function isEscaped(source, index) {
    let slashes = 0;
    for (let i = index - 1; i >= 0 && source[i] === '\\'; i--) slashes++;
    return slashes % 2 === 1;
  }

  function isCommented(source, index) {
    const lineStart = source.lastIndexOf('\n', index - 1) + 1;
    for (let i = lineStart; i < index; i++) {
      if (source[i] === '%' && !isEscaped(source, i)) return true;
    }
    return false;
  }

  function readBalanced(source, start, open, close) {
    if (source[start] !== open) return null;
    let depth = 0;
    for (let i = start; i < source.length; i++) {
      const char = source[i];
      if (char === '\\') {
        i++;
        continue;
      }
      if (char === '%' && !isEscaped(source, i)) {
        const newline = source.indexOf('\n', i + 1);
        if (newline === -1) break;
        i = newline;
        continue;
      }
      if (char === open) depth++;
      else if (char === close) {
        depth--;
        if (depth === 0) {
          return {
            start,
            end: i + 1,
            contentStart: start + 1,
            contentEnd: i,
            value: source.slice(start + 1, i),
          };
        }
      }
    }
    return null;
  }

  function findCommands(source, name, options) {
    const opts = Object.assign({ allowCommented: false }, options);
    const escapedName = String(name).replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    const pattern = new RegExp('\\\\' + escapedName + '(?![A-Za-z@])', 'g');
    const commands = [];
    let match;
    while ((match = pattern.exec(source))) {
      const start = match.index;
      if (source[start - 1] === '\\') continue;
      if (!opts.allowCommented && isCommented(source, start)) continue;

      const command = {
        name,
        start,
        end: pattern.lastIndex,
        args: [],
        optional: [],
      };
      let cursor = pattern.lastIndex;
      let malformed = false;

      while (true) {
        while (/\s/.test(source[cursor] || '')) cursor++;
        const char = source[cursor];
        if (char !== '{' && char !== '[') break;
        const part = readBalanced(source, cursor, char, char === '{' ? '}' : ']');
        if (!part) {
          malformed = true;
          break;
        }
        if (char === '{') command.args.push(part);
        else command.optional.push(part);
        command.end = part.end;
        cursor = part.end;
        pattern.lastIndex = cursor;
      }

      if (!malformed) {
        command.raw = source.slice(command.start, command.end);
        commands.push(command);
      }
    }
    return commands;
  }

  function findCommand(source, name, options) {
    return findCommands(source, name, options)[0] || null;
  }

  function getArgument(source, name, argumentIndex, options) {
    const command = findCommand(source, name, options);
    const index = argumentIndex || 0;
    return command && command.args[index] ? command.args[index].value : '';
  }

  function replaceArgument(source, command, argumentIndex, value) {
    const argument = command && command.args[argumentIndex];
    if (!argument) throw new Error(`Missing argument ${argumentIndex} for \\${command && command.name}`);
    return source.slice(0, argument.contentStart) + value + source.slice(argument.contentEnd);
  }

  function removeRange(source, start, end) {
    let nextEnd = end;
    if (source[nextEnd] === '\r') nextEnd++;
    if (source[nextEnd] === '\n') nextEnd++;
    return (source.slice(0, start) + source.slice(nextEnd)).replace(/\n{3,}/g, '\n\n');
  }

  function removeCommand(source, command) {
    return removeRange(source, command.start, command.end);
  }

  function upsertCommand(source, name, value) {
    const active = findCommand(source, name);
    if (active && active.args[0]) return replaceArgument(source, active, 0, value);

    const commented = findCommand(source, name, { allowCommented: true });
    if (commented) {
      const lineStart = source.lastIndexOf('\n', commented.start - 1) + 1;
      const indentation = (source.slice(lineStart, commented.start).match(/^\s*/) || [''])[0];
      return source.slice(0, lineStart) + indentation + `\\${name}{${value}}` + source.slice(commented.end);
    }

    return source.trimEnd() + `\n\\${name}{${value}}\n`;
  }

  function findEnvironment(source, name, offset) {
    const from = offset || 0;
    const escapedName = String(name).replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    const beginPattern = new RegExp('\\\\begin\\{\\s*' + escapedName + '\\s*\\}', 'g');
    beginPattern.lastIndex = from;
    let begin;
    while ((begin = beginPattern.exec(source))) {
      if (!isCommented(source, begin.index)) break;
    }
    if (!begin) return null;

    const token = new RegExp('\\\\(begin|end)\\{\\s*' + escapedName + '\\s*\\}', 'g');
    token.lastIndex = begin.index;
    let depth = 0;
    let match;
    while ((match = token.exec(source))) {
      if (isCommented(source, match.index)) continue;
      if (match[1] === 'begin') {
        depth++;
      } else {
        depth--;
        if (depth === 0) {
          return {
            name,
            start: begin.index,
            end: token.lastIndex,
            contentStart: begin.index + begin[0].length,
            contentEnd: match.index,
            content: source.slice(begin.index + begin[0].length, match.index),
          };
        }
      }
    }
    return null;
  }

  function itemizeLines(environment) {
    if (!environment) return '';
    return environment.content.replace(/^\s*\\item\s*/gm, '').trim();
  }

  function makeItemize(value) {
    const lines = String(value || '').split('\n').filter(line => line.trim());
    if (!lines.length) return '';
    return `\\begin{itemize}\n${lines.map(line => `  \\item ${line.trim()}`).join('\n')}\n\\end{itemize}`;
  }

  return {
    findCommands,
    findCommand,
    getArgument,
    replaceArgument,
    removeRange,
    removeCommand,
    upsertCommand,
    findEnvironment,
    itemizeLines,
    makeItemize,
    isCommented,
  };
});
