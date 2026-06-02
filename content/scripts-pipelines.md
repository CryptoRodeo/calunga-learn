---
id: scripts-pipelines
title: Key Scripts & Tekton Pipelines
---

### Scripts

<table>
<thead><tr><th>Script</th><th>Purpose</th></tr></thead>
<tbody>
  <tr><td><code>build-wheels</code></td><td>Main entry point: Fromager resolve &rarr; build &rarr; auditwheel &rarr; SBOM patch</td></tr>
  <tr><td><code>collect-build-files</code></td><td>Gathers SBOM + build artifacts from completed builds</td></tr>
  <tr><td><code>patch-sbom-purl</code></td><td>Adds file_name qualifier to PURLs, renames SBOM to <code>redhat.spdx.json</code></td></tr>
  <tr><td><code>check-for-updates.py</code></td><td>Async PyPI/Pulp version checker (index repo)</td></tr>
  <tr><td><code>identify-packages</code></td><td>Detects which package JSONs changed in PR</td></tr>
</tbody>
</table>

### Build Pipeline (17 tasks)

{{ diagram("flowchart LR
    init --> clone
    clone --> prefetch
    prefetch --> build[\"build-container\"]
    build --> idx[\"build-image-index\"]
    idx --> scans[\"Scans (parallel):\nClair | Snyk | Coverity\nShellCheck | Unicode\nClamAV | RPM sig\"]
    scans --> tags[\"apply-tags\"]
    tags --> push[\"push-dockerfile\"]
    push --> summary") }}

{{ callout("<strong>Tekton Pipelines:</strong> Builder = 8 CPU, 12GB RAM, 3h timeout &nbsp;|&nbsp; Utils = defaults, 1h timeout &nbsp;|&nbsp; Task bundle = defaults") }}
