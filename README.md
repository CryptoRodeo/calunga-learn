# Calunga Learn

Documentation site for Red Hat Trusted Libraries (RHTL), built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

## Quick Start

```bash
pip install -r requirements.txt
mkdocs serve
# Open http://localhost:8000
```

## Project Structure

```
calunga-learn/
├── mkdocs.yml                    # Site config, nav, extensions
├── requirements.txt              # mkdocs-material
├── docs/
│   ├── index.md                  # Landing page
│   ├── why.md                    # 23 content pages total
│   ├── getting-started.md
│   ├── ...
│   ├── stylesheets/
│   │   └── extra.css             # Red Hat dark theme overrides
│   ├── javascripts/
│   │   └── extra.js              # Mermaid theme config
│   └── includes/
│       └── glossary.md           # Auto-appended abbreviation definitions
└── .github/workflows/deploy.yml  # GitHub Pages deployment
```

## Editing Content

Edit any `.md` file in `docs/`, then preview with `mkdocs serve` (hot reload).

### Content Format

Standard Markdown with MkDocs Material extensions:

- **Admonitions:** `!!! note ""` (red-styled) or `!!! info ""` (teal-styled)
- **Grid cards:** `<div class="grid cards" markdown>` with list items
- **Mermaid diagrams:** fenced code blocks with `mermaid` language
- **Tables:** standard Markdown tables or raw HTML
- **Glossary tooltips:** automatic via abbreviation definitions in `docs/includes/glossary.md`

### Custom HTML Components

These use CSS classes from `docs/stylesheets/extra.css`:

| Component | Usage |
|-----------|-------|
| `.badge-row` / `.badge` | Row of pill badges |
| `.flow-steps` / `.flow-step` | Numbered flow steps with `.num` circles |
| `.security-grid` / `.security-item` | Icon + title + description grid |
| `.glossary-grid` / `.glossary-card` | Term definition cards |
| `.dir-tree` | Monospace directory tree block |
| `.subtitle` | Muted subtitle paragraph |

## Adding a New Page

1. Create `docs/new-page.md`
2. Add to the `nav` section in `mkdocs.yml`
3. Preview with `mkdocs serve`

## Building

```bash
mkdocs build    # Output in site/
```

## Deployment

Pushes to `main` trigger GitHub Actions → `mkdocs build` → GitHub Pages.

## Dependencies

- **Python 3.12+**
- **mkdocs-material** ≥ 9.5
