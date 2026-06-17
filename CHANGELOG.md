# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- SEO: `sitemap.xml`, `robots.txt`, JSON-LD structured data on landing page
- Accessibility: ARIA labels, keyboard focus indicators, semantic landmarks
- Service Worker update notification banner
- Autosave indicator in editor toolbar
- GitHub Token security warning in settings modal
- XSS-safe escaping for form inputs
- Dependabot configuration for GitHub Actions version updates
- Stale bot configuration for issue/PR triage
- Word/character counter in editor status bar
- LaTeX snippet insertion panel (common symbols, structures)
- Mobile-responsive improvements for editor layout
- Lazy-loading for PDF.js library
- Preconnect hints for CDN resources

### Changed
- Version bumped to v3.9.0
- Improved mobile viewport handling in editor
- Enhanced keyboard navigation throughout the app

## [3.8.0] - 2026-06-15

### Added
- Auto-detect GitHub repository owner from Pages URL
- SEO `og:url` and canonical URL meta tags
- Service Worker supports PDF list caching and navigation offline fallback
- `FORCE_JAVASCRIPT_ACTIONS_TO_NODE24=true` for Node.js 24 compatibility

### Changed
- Replaced placeholder usernames and via.placeholder links in README
- GitHub Pages switched from legacy to workflow deployment mode
- `build.yml` Commit PDFs step uses GitHub API instead of container git push

### Fixed
- CI failure caused by Pillow installation in Docker container
- Logo PNG generation now conditionally skipped when files exist in repo
- Git push permission issue (exit code 128) in CI container

## [3.7.0] - 2026-06-13

### Added
- Online editor with CodeMirror 6 syntax highlighting
- Form-based editing for all resume sections
- Theme selector with live preview
- Module toggle panel
- GitHub API-based build & deploy workflow
- Drag-and-drop `.tex` / `.json` file import
- Configuration export/import (JSON)
- Keyboard shortcuts panel
- PDF preview page with thumbnail sidebar
- Service Worker for offline support

### Changed
- Project migrated to standalone repository
- CI/CD fully automated via GitHub Actions

## [3.6.1] - 2026-06-06

### Added
- Header gradient decoration bar
- Skill tag gradient styling
- Card micro-shadow effect
- Section title icon round background
- Footer thin-line gradient
- Abstract left decoration line

### Fixed
- Font fallback chain compatibility for Linux distributions

## [3.6.0] - 2026-06-04

### Added
- 8 built-in theme colors + custom theme support
- 11 resume variants (academic, business, minimalist, etc.)
- Logo support for education/experience items (50+ placeholders)
- QR code embedding in footer
- Page overflow warning
- `[compact]`, `[monochrome]`, `[nofooter]`, `[en]` class options
- `build_placeholders.py` for automated logo generation
- Makefile with `all-pdf`, `clean`, `watch` targets

## [3.5.0] - 2026-05-20

### Added
- Initial modular architecture
- Separate `.tex` files for each resume section
- Centralized `config.tex` configuration
- Cross-platform font fallback (macOS / Linux / Windows)
- XeLaTeX compilation pipeline
