---
id: release-pipeline
title: Release Pipeline
---

After wheels pass security scans and Enterprise Contract checks, the release pipeline handles attestation, signing, and upload to the registry.

{{ diagram("flowchart LR
    wheels[\"Built Wheels\"] --> attest[\"Generate SLSA\nProvenance\"]
    attest --> sign[\"cosign sign\n(key-based)\"]
    sign --> pep740[\"Convert DSSE\nto PEP 740\"]
    pep740 --> check[\"Check if wheel\nexists in Pulp\"]
    check --> upload[\"Twine upload\n+ attestation\"]
    upload --> registry[\"packages.redhat.com\"]

    style wheels fill:#1a237e,color:#fff
    style sign fill:#c62828,color:#fff
    style registry fill:#1b5e20,color:#fff") }}

{{ two_col_start() }}
{{ card("Attestation Flow") }}

- SHA256 hash computed for each wheel
- SLSA v0.2 provenance predicate generated
- Signed with **cosign** (key from K8s secret)
- DSSE envelope converted to **PEP 740** format
- Attestation uploaded alongside wheel

{{ card_end() }}
{{ card("Upload Logic") }}

- **Skip** if wheel already exists in Pulp
- **Skip** if attestation file missing
- **Fail** if any upload errors or missing attestations
- Summary report: uploaded / skipped / failed counts

{{ card_end() }}
{{ two_col_end() }}

{{ callout("<strong>Auto-release:</strong> Configured with a <strong>7-day grace period</strong> via Konflux ReleasePlan. Standing attribution enabled - releases proceed automatically unless blocked.") }}
