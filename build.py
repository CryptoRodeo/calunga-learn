#!/usr/bin/env python3
"""Build index.html from Jinja templates and Markdown content files."""

import re
import sys
from pathlib import Path

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).parent
CONTENT_DIR = ROOT / "content"
TEMPLATE_DIR = ROOT / "templates"
OUTPUT = ROOT / "index.html"


def parse_frontmatter(text):
    """Split YAML frontmatter from body. Returns (metadata_dict, body_str)."""
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            meta = yaml.safe_load(parts[1]) or {}
            body = parts[2].strip()
            return meta, body
    return {}, text


def mermaid_post_process(html):
    """Convert <pre><code class="language-mermaid"> blocks to <div class="mermaid">."""
    pattern = r'<pre><code class="language-mermaid">(.*?)</code></pre>'
    return re.sub(
        pattern,
        lambda m: f'<div class="diagram-wrap"><div class="mermaid">\n{m.group(1)}\n</div></div>',
        html,
        flags=re.DOTALL,
    )


def build():
    sidebar_path = CONTENT_DIR / "_sidebar.yaml"
    sidebar = yaml.safe_load(sidebar_path.read_text())

    env = Environment(
        loader=FileSystemLoader(str(TEMPLATE_DIR)),
        autoescape=False,
    )

    macros_template = env.get_template("macros.html")
    macros_source = macros_template.module

    macro_env = Environment(loader=FileSystemLoader(str(TEMPLATE_DIR)), autoescape=False)
    macros_str = (TEMPLATE_DIR / "macros.html").read_text()

    md = markdown.Markdown(extensions=["fenced_code", "tables", "attr_list"])

    section_order = [item["href"] for item in sidebar if "href" in item]

    sections = []
    for href in section_order:
        filepath = CONTENT_DIR / f"{href}.md"
        if not filepath.exists():
            print(f"Warning: {filepath} not found, skipping", file=sys.stderr)
            continue

        raw = filepath.read_text()
        meta, body = parse_frontmatter(raw)

        jinja_src = macros_str + "\n" + body
        content_template = macro_env.from_string(jinja_src)
        rendered_jinja = content_template.render()

        md.reset()
        html = md.convert(rendered_jinja)

        html = mermaid_post_process(html)

        section_id = meta.get("id", href)
        title = meta.get("title")

        title_html = ""
        if title:
            title_html = f"<h2>{title}</h2>\n"

        sections.append({
            "id": section_id,
            "content": title_html + html,
        })

    base = env.get_template("base.html")
    output = base.render(sidebar=sidebar, sections=sections)

    OUTPUT.write_text(output)
    print(f"Built {OUTPUT} ({len(sections)} sections)")


if __name__ == "__main__":
    build()
