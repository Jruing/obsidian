# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **personal technical knowledge base (wiki)** authored in Chinese, covering AI tools, Linux, software development (Python, Golang, Java, frontend), databases, DevOps, and daily utilities. Content is written as Markdown files and published as a static site via **MkDocs + Material theme** to GitHub Pages.

- **Content language**: Chinese (zh-CN)
- **Site URL**: https://jruing.github.io/obsidian/
- **Repo**: https://github.com/jruing/obsidian

## Common Commands

### Local preview
```bash
mkdocs serve
```

### Build static site
```bash
mkdocs build
```

### Deploy to GitHub Pages
```bash
mkdocs gh-deploy --force
```

> **Note**: `mkdocs-material` is required. Install with `pip install mkdocs-material` if not already available.

## CI/CD

- **File**: `.github/workflows/main.yml`
- **Trigger**: Push or PR to any branch
- **Steps**: Checkout → Setup Python 3.10 → Install `mkdocs-material` → Deploy to GitHub Pages via `mkdocs gh-deploy --force`

## Content Structure

All source Markdown files live under `docs/`. The navigation is **explicitly defined** in `mkdocs.yml` under the `nav:` key—adding a new file requires updating `mkdocs.yml` for it to appear in the site.

Key top-level sections in `nav:`:
- `AI/` — AI tools, agents, MCP, prompts
- `Linux/` — Linux basics and commands
- `开发/` — Development (Golang, Python, Java, frontend)
- `数据库/` — Databases (MySQL, PostgreSQL, Redis)
- `日常工具/` — Daily utilities
- `运维/` — DevOps (Docker, K8s, Nginx, Jenkins, monitoring, etc.)

## Writing Conventions

- **Frontmatter**: Each note should include YAML frontmatter with `title`, `date`, and `tags`.
  ```yaml
  ---
  title: "笔记标题"
  date: 2026-06-11
  tags:
    - 标签1
    - 标签2
  ---
  ```
- **Language**: Content is in Chinese.
- **Links**: Prefer relative links between notes; external links are fine.
- **Images**: Store in `docs/` or reference via absolute/relative paths.

## Obsidian Integration

- The `docs/` folder is also an **Obsidian vault** (`.obsidian/` contains workspace and plugin settings).
- Obsidian plugins in use: Excalidraw, Calendar, Icon Folder, Style Settings, Editing Toolbar.
- Core plugins enabled: File Explorer, Global Search, Graph, Backlinks, Canvas, Tags, Properties, Daily Notes, Templates, etc.
- **Do not commit** `.obsidian/workspace.json` or plugin caches. `.gitignore` already excludes `*/.obsidian/*` and `database.sqlite`.

## Important Files

| File | Purpose |
|------|---------|
| `mkdocs.yml` | Site configuration, theme settings, and navigation (`nav:`) |
| `docs/readme.md` | Entry point / overview page |
| `.github/workflows/main.yml` | Auto-deploy to GitHub Pages |
| `docs/.obsidian/` | Obsidian vault settings (not committed) |
