---
id: e2e-flow
title: End-to-End Flow
---

{{ diagram("flowchart TD
    PyPI[(PyPI)] --> Cron[\"check-for-updates.py\n(12h cron)\"]
    Pulp[(Red Hat Pulp)] --> Cron
    Cron --> PRs[\"Auto-create PRs\n(one per package)\"]
    PRs -->|auto-merge| Build[\"build-python-wheels\n(Fromager + auditwheel)\"]
    Build --> Scan[\"Security Scans\nClair | Snyk | ClamAV\nCoverity | ShellCheck\"]
    Scan --> ECP[\"Enterprise Contract\nPolicy check\"]
    ECP --> Sign[\"Attestation\n(cosign signing)\"]
    Sign --> Release[\"Auto-release\n(7-day grace)\"]
    Release --> Registry[\"packages.redhat.com\"]
    Registry --> Users[\"pip install / uv\"]

    style PyPI fill:#1565c0,color:#fff
    style Pulp fill:#1565c0,color:#fff
    style Registry fill:#2e7d32,color:#fff
    style Users fill:#2e7d32,color:#fff
    style Scan fill:#c62828,color:#fff
    style ECP fill:#c62828,color:#fff") }}
