# Why Calunga?

<div class="grid cards" markdown>

-   __The Problem__{ style="color:#ee0000;" }

    ---

    - PyPI wheels are pre-built binaries - you trust the uploader
    - No guarantee of source-to-binary correspondence
    - Supply chain attacks on popular packages (typosquatting, account takeover)
    - No embedded SBOM or provenance metadata
    - Enterprise compliance requires verifiable supply chains

-   __Calunga's Answer__{ style="color:#3e8635;" }

    ---

    - **Build from source** - 17 C/C++ libs + Python compiled in trusted environments
    - **SBOM in every wheel** - CycloneDX `redhat.spdx.json`
    - **6 security scans** per build (Clair, Snyk, ClamAV, Coverity, ShellCheck, Unicode)
    - **Enterprise Contract Policy** - Red Hat compliance enforcement
    - **Attestation & signing** - cosign provenance
    - **Hermetic builds** - optional zero-network mode

</div>
