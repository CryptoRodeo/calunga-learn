---
id: supply-chain
title: Supply Chain Security
---

{{ security_grid_start() }}
{{ security_item("&#x1f512;", "Hash Pinning", "All Python deps use --require-hashes. Container/task refs pinned by SHA256.") }}
{{ security_item("&#x1f3d7;&#xfe0f;", "Source Builds", "17 C/C++ libs compiled from source with verified checksums. No pre-built binaries.") }}
{{ security_item("&#x1f4cb;", "SBOM Embedding", "Every wheel contains redhat.spdx.json with supplier info and PURLs.") }}
{{ security_item("&#x1f50d;", "Security Scanning", "6 scans per build: Clair, Snyk, ClamAV, Coverity, ShellCheck, Unicode.") }}
{{ security_item("&#x1f4dc;", "Enterprise Contract Policy", "Red Hat compliance enforcement on every release.") }}
{{ security_item("&#x270d;&#xfe0f;", "Attestation", "Provenance and signing via cosign (Sigstore).") }}
{{ security_item("&#x1f3e0;", "Hermetic Builds", "Optional fully isolated mode - zero network access during build.") }}
{{ security_item("&#x1f4e6;", glossary("OCI Trusted Artifacts", "Konflux pattern for passing data between Tekton tasks via OCI artifacts stored in a registry, instead of shared PersistentVolumeClaims. Provides immutability and auditability."), "Data passes between tasks via OCI artifacts, not shared volumes.") }}
{{ security_grid_end() }}
