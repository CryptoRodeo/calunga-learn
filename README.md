# Calunga Learn

Documentation site for Red Hat Trusted Libraries (RHTL), built from Markdown content files using Jinja2 templates and a Python build script.

## Quick Start

```bash
pip install -r requirements.txt
python build.py
```

This generates `index.html` from the content files. Serve locally with:

```bash
python3 -m http.server 8765
# Open http://localhost:8765/index.html
```

> **Note:** The CSS is an external file (`static/style.css`), so opening `index.html` directly via `file://` won't load styles. Use an HTTP server.

## Project Structure

```
calunga-learn/
├── build.py                 # Build script — generates index.html
├── requirements.txt         # Python deps: jinja2, markdown, pyyaml
├── index.html               # OUTPUT (generated — do not edit directly)
├── templates/
│   ├── base.html            # Page shell: sidebar, JS, Mermaid config
│   └── macros.html          # Reusable Jinja macros for structured elements
├── content/
│   ├── _sidebar.yaml        # Sidebar navigation structure
│   ├── overview.md          # Each .md = one page section
│   ├── why.md
│   ├── getting-started.md
│   └── ...                  # 22 content files total
└── static/
    └── style.css            # Extracted CSS
```

## How It Works

The build pipeline processes each Markdown file through three stages:

1. **Parse frontmatter** — YAML header defines the section `id` and `title`
2. **Render Jinja macros** — Expands macro calls (callouts, cards, diagrams, etc.) into HTML
3. **Convert Markdown to HTML** — Standard Markdown processing with fenced code blocks and tables

The rendered sections are injected into `templates/base.html` in the order defined by `content/_sidebar.yaml`.

```
content/*.md  →  Jinja render  →  Markdown→HTML  →  base.html  →  index.html
```

## Editing Content

Edit any `.md` file in `content/`, then run `python build.py`.

### Content File Format

Each file has YAML frontmatter and a Markdown body:

```markdown
---
id: my-section
title: My Section Title
---

Some markdown content here.

- Bullet points work
- **Bold** and `code` work

{{ callout("Important note here.") }}
```

- `id` — Used as the HTML `<section id="...">` and sidebar anchor
- `title` — Rendered as an `<h2>`. Omit for sections that use `<h1>` (like the overview)

## Available Macros

Use these in any `.md` file. Defined in `templates/macros.html`.

### Layout

| Macro | Usage |
|-------|-------|
| `two_col_start()` / `two_col_end()` | Two-column grid wrapper |
| `card("Title", color="teal")` / `card_end()` | Card with colored header. Colors: `teal` (default), `red`, `green` |
| `subtitle("text")` | Muted subtitle paragraph |

### Content Elements

| Macro | Usage |
|-------|-------|
| `callout("text", style="red")` | Callout box. Styles: `red` (default), `teal` |
| `badge_row(["a", "b", "c"])` | Row of pill badges |
| `flow_steps_start()` / `flow_steps_end()` | Flow step container |
| `flow_step(1, "Description", color="red")` | Numbered step. Colors: `red` (default), `teal` |
| `glossary("Term", "Definition tooltip")` | Inline glossary term with hover tooltip |
| `dir_tree("formatted html")` | Monospace directory tree block |

### Diagrams

| Macro | Usage |
|-------|-------|
| `diagram("mermaid code here")` | Wrapped Mermaid diagram with styling |

### Security & Glossary Grids

| Macro | Usage |
|-------|-------|
| `security_grid_start()` / `security_grid_end()` | Security feature grid |
| `security_item("🔒", "Title", "Description")` | Grid item with icon |
| `glossary_grid_start()` / `glossary_grid_end()` | Glossary card grid |
| `glossary_card("gl-id", "Term", "Definition")` | Glossary reference card |

### Example: Section with Diagram and Callout

```markdown
---
id: my-flow
title: My Flow
---

Here's how it works:

{{ diagram("flowchart LR
    A --> B --> C
    style A fill:#1a237e,color:#fff") }}

{{ callout("<strong>Note:</strong> Step B is optional.", style="teal") }}
```

## Adding a New Section

1. Create `content/new-section.md` with frontmatter
2. Add an entry to `content/_sidebar.yaml`:
   ```yaml
   - label: My New Section
     href: new-section
   ```
   For a section divider:
   ```yaml
   - section: Category Name
   ```
3. Run `python build.py`

The section order in the output matches the order in `_sidebar.yaml`.

## Modifying Styles

Edit `static/style.css`. No rebuild needed — just refresh the browser.

## Adding New Macros

1. Define the macro in `templates/macros.html`:
   ```jinja
   {% macro my_macro(arg1, arg2="default") %}
   <div class="my-class">{{ arg1 }}</div>
   {% endmacro %}
   ```
2. Add CSS for any new classes to `static/style.css`
3. Use in content files: `{{ my_macro("hello") }}`
4. Run `python build.py`

## Dependencies

- **Python 3.8+**
- **Jinja2** — template rendering and macros
- **Markdown** — `.md` to HTML conversion
- **PyYAML** — frontmatter and sidebar config parsing
