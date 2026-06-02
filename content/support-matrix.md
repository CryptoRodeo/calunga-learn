---
id: support-matrix
title: Support Matrix & Roadmap
---

{{ two_col_start() }}
{{ card("Python Versions") }}

<table>
<thead><tr><th>Version</th><th>Status</th></tr></thead>
<tbody>
  <tr><td>Python 2.x</td><td style="color:#f44;">Not supported</td></tr>
  <tr><td>Python 3.9 – 3.10</td><td style="color:#f44;">Not supported</td></tr>
  <tr><td><strong>Python 3.12</strong></td><td style="color:var(--rh-green);">Fully supported</td></tr>
  <tr><td>Python 3.11, 3.13, 3.14</td><td style="color:var(--rh-gold);">Planned</td></tr>
</tbody>
</table>

{{ card_end() }}
{{ card("Architectures") }}

<table>
<thead><tr><th>Arch</th><th>Status</th></tr></thead>
<tbody>
  <tr><td><strong>x86_64</strong></td><td style="color:var(--rh-green);">Fully supported</td></tr>
  <tr><td>aarch64</td><td style="color:var(--rh-gold);">Planned</td></tr>
</tbody>
</table>

### Manylinux Target

Primary: `manylinux_2_28` (glibc 2.28+, RHEL 8+).
Some wheels also carry `manylinux_2_27` compatibility.

{{ card_end() }}
{{ two_col_end() }}

### Alternative Python Runtimes

The builder image includes multiple Python runtimes beyond CPython, all SHA256-pinned:

<table>
<thead><tr><th>Runtime</th><th>Versions</th><th>Architectures</th></tr></thead>
<tbody>
  <tr><td><strong>CPython</strong></td><td>3.12.12 (from source)</td><td>x86_64, aarch64</td></tr>
  <tr><td><strong>PyPy</strong></td><td>3.8 – 3.11</td><td>x86_64, aarch64, i686</td></tr>
  <tr><td><strong>GraalPy</strong></td><td>3.11 (24.2.2), 3.12 (25.0.1)</td><td>x86_64, aarch64</td></tr>
</tbody>
</table>

{{ callout("All interpreter downloads are pinned by SHA256 hash in <code>python_versions.json</code> for reproducibility.") }}
