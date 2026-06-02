# Release Pipeline

After wheels pass security scans and Enterprise Contract checks, the release pipeline handles attestation, signing, and upload to the registry.

```mermaid
flowchart LR
    wheels["Built Wheels"] --> attest["Generate SLSA<br>Provenance"]
    attest --> sign["cosign sign<br>(key-based)"]
    sign --> pep740["Convert DSSE<br>to PEP 740"]
    pep740 --> check["Check if wheel<br>exists in Pulp"]
    check --> upload["Twine upload<br>+ attestation"]
    upload --> registry["packages.redhat.com"]

    style wheels fill:#1a237e,color:#fff
    style sign fill:#c62828,color:#fff
    style registry fill:#1b5e20,color:#fff
```

<div class="grid cards" markdown>

-   __Attestation Flow__{ style="color:#009596;" }

    ---

    - SHA256 hash computed for each wheel
    - SLSA v0.2 provenance predicate generated
    - Signed with **cosign** (key from K8s secret)
    - DSSE envelope converted to **PEP 740** format
    - Attestation uploaded alongside wheel

-   __Upload Logic__{ style="color:#009596;" }

    ---

    - **Skip** if wheel already exists in Pulp
    - **Skip** if attestation file missing
    - **Fail** if any upload errors or missing attestations
    - Summary report: uploaded / skipped / failed counts

</div>

!!! note ""

    **Auto-release:** Configured with a **7-day grace period** via Konflux ReleasePlan. Standing attribution enabled - releases proceed automatically unless blocked.
