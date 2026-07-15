---
id: builder-deep-dive
title: "Builder Image: Source-Built Libraries"
---

{{ two_col_start() }}
<div markdown="1">
<table>
<thead><tr><th>Library</th><th>Version</th><th>Why</th></tr></thead>
<tbody>
  <tr><td>OpenSSL</td><td>3.5.4</td><td>TLS, cryptography wheels</td></tr>
  <tr><td>curl</td><td>8.17.0</td><td>HTTP client for downloads</td></tr>
  <tr><td>git</td><td>2.51.2</td><td>Source fetching</td></tr>
  <tr><td>SQLite</td><td>3.51.0</td><td>Python stdlib module</td></tr>
  <tr><td>OpenBLAS</td><td>latest</td><td>NumPy/SciPy linear algebra</td></tr>
  <tr><td>libjpeg-turbo</td><td>latest</td><td>Pillow image processing</td></tr>
  <tr><td>libxml2 / libxslt</td><td>latest</td><td>lxml XML parsing</td></tr>
  <tr><td>libyaml</td><td>latest</td><td>PyYAML C extension</td></tr>
  <tr><td>zlib / bzip2 / zstd</td><td>latest</td><td>Compression</td></tr>
  <tr><td>libffi</td><td>latest</td><td>ctypes / cffi</td></tr>
  <tr><td>mpdecimal</td><td>latest</td><td>Python decimal module</td></tr>
  <tr><td>libomp</td><td>latest</td><td>OpenMP parallelism</td></tr>
  <tr><td>libpng / libtiff</td><td>latest</td><td>Image format support</td></tr>
  <tr><td>Tcl/Tk</td><td>8.6.17</td><td>CPython stdlib GUI module</td></tr>
  <tr><td>libxcrypt</td><td>4.5.1</td><td>crypt() password hashing</td></tr>
</tbody>
</table>
</div>
<div markdown="1">

{{ card("Build Details") }}

- **Base:** UBI8 (RHEL 8 userspace)
- **Python:** CPython 3.12.12 from source
- **Alt runtime:** PyPy 3.11
- **C/C++:** gcc-toolset-14
- **C/C++ (static):** clang 21.1.5
- **Rust:** 1.95.0
- **Deps:** {{ glossary("pip-compile", "Dependency resolver from pip-tools. Generates fully pinned requirements.txt with SHA256 hashes from a loose requirements.in, ensuring reproducible installs.") }} --require-hashes

{{ card_end() }}

{{ card("Key Tools") }}

- **{{ glossary("Fromager", "Python wheel build orchestrator. Resolves full dependency graph from source distributions, builds each package in order, and embeds CycloneDX SBOMs.") }}** - orchestrates full dep graph builds
- **{{ glossary("auditwheel", "Post-build compliance tool. Inspects Linux wheels for shared library deps, bundles required .so files, relabels with correct manylinux platform tag.") }}** - bundles .so, sets manylinux tag
- **pip-compile** - hash-pinned requirements

{{ card_end() }}
</div>
{{ two_col_end() }}
