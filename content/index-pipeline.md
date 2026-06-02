---
id: index-pipeline
title: Index Build Pipeline
---

{{ diagram("flowchart LR
    clone[\"clone-repository\"] --> identify[\"identify-packages\"]
    identify --> wheels[\"build-wheels\"]
    wheels --> scans

    subgraph scans[\"Security Scans (parallel)\"]
        direction TB
        clair[\"Clair\"]
        snyk[\"Snyk SAST\"]
        coverity[\"Coverity\"]
        shell[\"ShellCheck\"]
        clamav[\"ClamAV\"]
    end

    scans --> ecp[\"Enterprise Contract\"]
    ecp --> release[\"Auto-release\"]

    style scans fill:#400,color:#fff
    style release fill:#143,color:#fff") }}

{{ two_col_start() }}
{{ card("Build Resources") }}

- **Memory:** 20GB for wheel builds
- **Task:** `build-python-wheels-oci-ta`
- **Image:** pinned by SHA256 digest

{{ card_end() }}
{{ card("Output") }}

- IMAGE_URL — built wheel OCI artifact
- IMAGE_DIGEST — SHA256 of artifact
- GIT_COMMIT — source commit hash

{{ card_end() }}
{{ two_col_end() }}
