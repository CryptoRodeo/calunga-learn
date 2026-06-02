---
id: glossary
title: Technology Glossary
---

{{ glossary_grid_start() }}
{{ glossary_card("gl-fromager", "Fromager", "Python wheel build orchestrator. Resolves full dependency graph from source distributions, builds each package in order, embeds CycloneDX SBOMs. Ensures wheels built from source — not pre-built from PyPI.") }}
{{ glossary_card("gl-auditwheel", "auditwheel", "Post-build compliance tool. Inspects Linux wheels for shared library deps, bundles required .so files, relabels with correct manylinux platform tag (e.g., manylinux_2_28).") }}
{{ glossary_card("gl-tekton", "Tekton", "Kubernetes-native CI/CD. Pipelines defined as YAML CRDs (Tasks, Pipelines, PipelineRuns). Each step runs in its own container. Used here via Konflux.") }}
{{ glossary_card("gl-konflux", "Konflux", "Red Hat's enterprise CI/CD on Tekton. Adds Enterprise Contract Policy, release management, nudge-based auto-updates, and OCI Trusted Artifacts.") }}
{{ glossary_card("gl-buildah", "Buildah", "Daemonless container builder. Builds OCI/Docker images from Containerfiles without Docker daemon. Used by Tekton tasks for builder/utils images.") }}
{{ glossary_card("gl-twine", "Twine", "Python package upload tool. Publishes wheels to PyPI-compatible registries (here: Red Hat's Pulp at packages.redhat.com).") }}
{{ glossary_card("gl-ubi", "UBI", "Universal Base Image. Red Hat's freely redistributable minimal container base. UBI8 = RHEL 8 userspace (builder), UBI10 = RHEL 10 (utils/index).") }}
{{ glossary_card("gl-pip-compile", "pip-compile", "Dependency resolver (pip-tools). Generates pinned requirements.txt with SHA256 hashes from loose requirements.in. Ensures reproducible installs.") }}
{{ glossary_card("gl-oci-ta", "OCI Trusted Artifacts", "Konflux pattern: pass data between Tekton tasks via OCI artifacts in a registry, not shared PVCs. Immutable and auditable.") }}
{{ glossary_card("gl-cosign", "cosign", "Sigstore tool for signing/verifying container images and artifacts. Used for attestation and provenance in the release pipeline.") }}
{{ glossary_card("gl-pulp", "Pulp", "Red Hat's repository management platform. Hosts the RHTL Python package index. Version-detection cron checks Pulp for already-published versions.") }}
{{ glossary_card("gl-ecp", "Enterprise Contract Policy (ECP)", "Konflux policy framework. Validates builds meet Red Hat compliance (provenance, signatures, SBOM) before allowing releases.") }}
{{ glossary_card("gl-cyclonedx", "CycloneDX / SPDX", "SBOM standards. Fromager generates CycloneDX SBOMs embedded as redhat.spdx.json, listing components and provenance.") }}
{{ glossary_card("gl-manylinux", "manylinux", "PEP-defined Linux wheel compatibility standard. Specifies max glibc version and allowed shared libs. manylinux_2_28 = glibc 2.28+ (RHEL 8+).") }}
{{ glossary_card("gl-gcc", "gcc-toolset-14", "Red Hat's SCL-packaged GCC 14 for UBI8/RHEL 8. Modern C/C++ compilation without replacing system GCC.") }}
{{ glossary_card("gl-nudge", "Nudge", "Konflux auto-update mechanism. When plumbing publishes new image/task digest, nudge creates PRs in downstream repos to update pinned SHA256 refs.") }}
{{ glossary_card("gl-graalpy", "GraalPy", "Oracle's Python implementation on GraalVM. Supports 3.11 and 3.12. Included in builder for alternative runtime wheel compatibility testing. SHA256-pinned downloads.") }}
{{ glossary_card("gl-pep740", "PEP 740", "Python standard for digital attestations on packages. Defines how provenance metadata is attached to wheels for upload to PyPI-compatible registries. Calunga converts DSSE envelopes to PEP 740 format.") }}
{{ glossary_grid_end() }}
