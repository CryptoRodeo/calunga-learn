---
id: overview
---

# Calunga

{{ subtitle("Red Hat Trusted Libraries (RHTL) - Secure Python supply chain, from source to <code>pip install</code>") }}

{{ badge_row(["1,547+ packages", "manylinux_2_28", "Python 3.12", "SLSA provenance", "CycloneDX SBOM", "6 security scans", "Source-built"]) }}

Calunga is Red Hat's initiative for building, verifying, and distributing secure Python wheels. Seven repositories form a complete supply chain pipeline - **plumbing** provides build infrastructure, **index** manages the package catalog and triggers builds, supported by companion repos for npm packaging, source verification, CI analysis, prioritization, and wheel patching.
