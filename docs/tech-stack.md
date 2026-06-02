# Technology Stack

<table>
<thead><tr><th>Layer</th><th>Technology</th><th>Role</th></tr></thead>
<tbody>
  <tr><td><strong>Languages</strong></td><td>Bash, Python 3.12, YAML</td><td>Scripts, automation, pipeline definitions</td></tr>
  <tr><td><strong>Container Base</strong></td><td>UBI8 (builder), UBI10 (utils/index)</td><td>Red Hat Universal Base Images</td></tr>
  <tr><td><strong>CI/CD</strong></td><td>Tekton + Konflux</td><td>Kubernetes-native pipelines with enterprise features</td></tr>
  <tr><td><strong>Container Build</strong></td><td>Buildah</td><td>Daemonless OCI image builder</td></tr>
  <tr><td><strong>Wheel Builder</strong></td><td>Fromager (&ge;0.81.0)</td><td>Source-only wheel build orchestrator</td></tr>
  <tr><td><strong>Compliance</strong></td><td>auditwheel</td><td>manylinux repair & .so bundling</td></tr>
  <tr><td><strong>Security</strong></td><td>Clair, Snyk, ClamAV, Coverity, ShellCheck</td><td>6 scan types per build</td></tr>
  <tr><td><strong>SBOM</strong></td><td>CycloneDX / SPDX</td><td>Software Bill of Materials in every wheel</td></tr>
  <tr><td><strong>Registries</strong></td><td>Quay.io, packages.redhat.com</td><td>Images & wheels</td></tr>
  <tr><td><strong>Automation</strong></td><td>GitHub Actions, Nudge</td><td>Version detection & dependency updates</td></tr>
  <tr><td><strong>Compilers</strong></td><td>gcc-toolset-14, clang 21.1.5, Rust 1.95.0</td><td>Native extension compilation</td></tr>
</tbody>
</table>
