---
id: shared-infra
title: Shared Infrastructure
---

<table>
<thead><tr><th>Resource</th><th>Plumbing</th><th>Index</th></tr></thead>
<tbody>
  <tr><td><strong>Quay.io tenant</strong></td><td>calunga-tenant (images + bundles)</td><td>calunga-tenant (release artifacts)</td></tr>
  <tr><td><strong>Konflux app</strong></td><td>calunga-v2-plumbing</td><td>calunga-v2-index-main</td></tr>
  <tr><td><strong>Enterprise Contract</strong></td><td>Enforced on builder images</td><td>Enforced on wheel releases</td></tr>
  <tr><td><strong>{{ glossary("Nudge", "Konflux auto-update mechanism. When plumbing publishes a new image or task bundle digest, nudge creates PRs in downstream repos to update pinned SHA256 references.") }} auto-updates</strong></td><td>Updates builder image refs in index</td><td>Updates task bundle refs</td></tr>
</tbody>
</table>

{{ callout("<strong>Fully automated pipeline:</strong> upstream Python release &rarr; version detection &rarr; source build &rarr; security scan &rarr; compliance check &rarr; attestation &rarr; auto-release &rarr; packages.redhat.com") }}
