---
id: quick-ref
title: Quick Reference
---

{{ two_col_start() }}
<div markdown="1">

### Key Paths (Plumbing)

<table>
<tbody>
  <tr><td><code>builder/Containerfile</code></td><td>Main builder image (393 lines)</td></tr>
  <tr><td><code>builder/scripts/build-wheels</code></td><td>Wheel build entry point</td></tr>
  <tr><td><code>builder/build_scripts/</code></td><td>21 library build scripts</td></tr>
  <tr><td><code>builder/requirements.txt</code></td><td>Hash-pinned Fromager deps</td></tr>
  <tr><td><code>tasks/build-python-wheels-oci-ta.yaml</code></td><td>Tekton task definition</td></tr>
  <tr><td><code>pipelines/wheel-integration-test.yaml</code></td><td>Cross-OS test pipeline</td></tr>
  <tr><td><code>utils/scripts/pulp-upload</code></td><td>Pulp registry upload with attestation</td></tr>
  <tr><td><code>utils/scripts/generate-and-sign-attestations</code></td><td>cosign attestation + PEP 740 conversion</td></tr>
  <tr><td><code>.tekton/</code></td><td>PipelineRun definitions</td></tr>
</tbody>
</table>

### Key Paths (Index)

<table>
<tbody>
  <tr><td><code>onboarded_packages/*.json</code></td><td>1,547 package definitions</td></tr>
  <tr><td><code>hack/check-for-updates.py</code></td><td>Version detection script</td></tr>
  <tr><td><code>hack/identify-packages</code></td><td>Changed-package detector</td></tr>
  <tr><td><code>hack/onboard_package.py</code></td><td>New package onboarding script</td></tr>
  <tr><td><code>hack/onboard.sh</code></td><td>Package onboarding shell wrapper</td></tr>
  <tr><td><code>hack/batch-onboard.sh</code></td><td>Bulk package onboarding</td></tr>
  <tr><td><code>hack/build-locally.sh</code></td><td>Local development build</td></tr>
  <tr><td><code>hack/debug-package.sh</code></td><td>Package build debugging</td></tr>
  <tr><td><code>hack/generate-available-packages.py</code></td><td>Available packages list generator</td></tr>
  <tr><td><code>hack/merge-bot</code></td><td>Auto-merge eligible PRs</td></tr>
  <tr><td><code>hack/rebase-version-prs</code></td><td>Rebase version update PRs</td></tr>
  <tr><td><code>hack/replace-package</code></td><td>Replace existing package definition</td></tr>
  <tr><td><code>hack/retry-onpush.sh</code></td><td>Retry failed on-push builds</td></tr>
  <tr><td><code>.tekton/build-pipeline.yaml</code></td><td>Main build pipeline</td></tr>
  <tr><td><code>konflux/ecp.yaml</code></td><td>Enterprise Contract Policy</td></tr>
</tbody>
</table>

</div>
<div markdown="1">

### User Configuration

```
# pip.conf
[global]
extra-index-url =
    https://packages.redhat.com/trusted-libraries/python/simple/
```

```
# pyproject.toml (uv)
[[tool.uv.index]]
url = "https://packages.redhat.com/trusted-libraries/python/simple/"
name = "rhtl"
```

### Key Numbers

<table>
<tbody>
  <tr><td>Packages</td><td><strong>1,547+</strong></td></tr>
  <tr><td>Source-built libs</td><td><strong>17</strong></td></tr>
  <tr><td>Security scans</td><td><strong>6 types</strong></td></tr>
  <tr><td>Test OS targets</td><td><strong>6</strong></td></tr>
  <tr><td>Pipeline tasks</td><td><strong>18</strong></td></tr>
  <tr><td>Version check interval</td><td><strong>12 hours</strong></td></tr>
  <tr><td>Release grace period</td><td><strong>7 days</strong></td></tr>
</tbody>
</table>

</div>
{{ two_col_end() }}
