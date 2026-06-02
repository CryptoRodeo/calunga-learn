# Shared Infrastructure

<table>
<thead><tr><th>Resource</th><th>Plumbing</th><th>Index</th></tr></thead>
<tbody>
  <tr><td><strong>Quay.io tenant</strong></td><td>calunga-tenant (images + bundles)</td><td>calunga-tenant (release artifacts)</td></tr>
  <tr><td><strong>Konflux app</strong></td><td>calunga-v2-plumbing</td><td>calunga-v2-index-main</td></tr>
  <tr><td><strong>Enterprise Contract</strong></td><td>Enforced on builder images</td><td>Enforced on wheel releases</td></tr>
  <tr><td><strong>Nudge auto-updates</strong></td><td>Updates builder image refs in index</td><td>Updates task bundle refs</td></tr>
</tbody>
</table>

!!! note ""

    **Fully automated pipeline:** upstream Python release → version detection → source build → security scan → compliance check → attestation → auto-release → packages.redhat.com
