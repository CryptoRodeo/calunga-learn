---
id: why
title: Why Calunga?
---

{{ two_col_start() }}
{{ card("The Problem", color="red") }}

- PyPI wheels are pre-built binaries — you trust the uploader
- No guarantee of source-to-binary correspondence
- Supply chain attacks on popular packages (typosquatting, account takeover)
- No embedded SBOM or provenance metadata
- Enterprise compliance requires verifiable supply chains

{{ card_end() }}
{{ card("Calunga's Answer", color="green") }}

- **Build from source** — 17 C/C++ libs + Python compiled in trusted environments
- **SBOM in every wheel** — {{ glossary("CycloneDX", "SBOM standard. Fromager generates CycloneDX SBOMs embedded as redhat.spdx.json, listing all components and their provenance.") }} `redhat.spdx.json`
- **6 security scans** per build (Clair, Snyk, ClamAV, Coverity, ShellCheck, Unicode)
- **{{ glossary("Enterprise Contract Policy", "Konflux policy framework. Validates that builds meet Red Hat compliance requirements (provenance, signatures, SBOM presence) before allowing releases.") }}** — Red Hat compliance enforcement
- **Attestation & signing** — {{ glossary("cosign", "Sigstore tool for signing and verifying container images and artifacts. Used for attestation and provenance in the release pipeline.") }} provenance
- **Hermetic builds** — optional zero-network mode

{{ card_end() }}
{{ two_col_end() }}
