---
id: tech-stack
title: Technology Stack
---

<table>
<thead><tr><th>Layer</th><th>Technology</th><th>Role</th></tr></thead>
<tbody>
  <tr><td><strong>Languages</strong></td><td>Bash, Python 3.12, YAML</td><td>Scripts, automation, pipeline definitions</td></tr>
  <tr><td><strong>Container Base</strong></td><td>{{ glossary("UBI8", "Universal Base Image. Red Hat's freely redistributable, minimal container base image. UBI8 provides a RHEL 8 userspace for the builder image.") }} (builder), UBI10 (utils/index)</td><td>Red Hat Universal Base Images</td></tr>
  <tr><td><strong>CI/CD</strong></td><td>{{ glossary("Tekton", "Kubernetes-native CI/CD framework. Pipelines defined as YAML CRDs (Tasks, Pipelines, PipelineRuns). Each step runs in its own container.") }} + {{ glossary("Konflux", "Red Hat's enterprise CI/CD platform built on Tekton. Adds Enterprise Contract Policy enforcement, release management, nudge-based auto-updates, and OCI Trusted Artifacts.") }}</td><td>Kubernetes-native pipelines with enterprise features</td></tr>
  <tr><td><strong>Container Build</strong></td><td>{{ glossary("Buildah", "Daemonless container image builder. Builds OCI/Docker images from Containerfiles without requiring a Docker daemon. Used by Tekton tasks to produce the builder and utils images.") }}</td><td>Daemonless OCI image builder</td></tr>
  <tr><td><strong>Wheel Builder</strong></td><td>{{ glossary("Fromager", "Python wheel build orchestrator. Resolves full dependency graph from source distributions, builds each package in order, and embeds CycloneDX SBOMs.") }} (&ge;0.81.0)</td><td>Source-only wheel build orchestrator</td></tr>
  <tr><td><strong>Compliance</strong></td><td>{{ glossary("auditwheel", "Post-build compliance tool. Inspects Linux wheels for shared library dependencies, bundles required .so files, and relabels with the correct manylinux platform tag.") }}</td><td>{{ glossary("manylinux", "PEP-defined platform compatibility standard for Linux Python wheels. Specifies maximum glibc version and allowed shared library dependencies. manylinux_2_28 targets glibc 2.28+ (RHEL 8+).") }} repair & .so bundling</td></tr>
  <tr><td><strong>Security</strong></td><td>Clair, Snyk, ClamAV, Coverity, ShellCheck</td><td>6 scan types per build</td></tr>
  <tr><td><strong>SBOM</strong></td><td>{{ glossary("CycloneDX / SPDX", "SBOM standards. Fromager generates CycloneDX SBOMs embedded in each wheel as redhat.spdx.json, listing all components and their provenance.") }}</td><td>Software Bill of Materials in every wheel</td></tr>
  <tr><td><strong>Registries</strong></td><td>Quay.io, packages.redhat.com</td><td>Images & wheels</td></tr>
  <tr><td><strong>Automation</strong></td><td>GitHub Actions, {{ glossary("Nudge", "Konflux auto-update mechanism. When plumbing publishes a new image or task bundle digest, nudge creates PRs in downstream repos to update pinned SHA256 references.") }}</td><td>Version detection & dependency updates</td></tr>
  <tr><td><strong>Compilers</strong></td><td>{{ glossary("gcc-toolset-14", "Red Hat's SCL-packaged GCC 14 compiler suite for UBI8/RHEL 8. Provides modern C/C++ compilation without replacing system GCC.") }}, clang 21.1.5, Rust 1.95.0</td><td>Native extension compilation</td></tr>
</tbody>
</table>
