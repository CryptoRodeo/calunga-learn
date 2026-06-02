---
id: version-detection
title: Automated Version Detection
---

{{ diagram("sequenceDiagram
    participant GH as GitHub Actions (12h cron)
    participant Script as check-for-updates.py
    participant PyPI as PyPI
    participant Pulp as Red Hat Pulp
    participant Repo as calunga-project-index

    GH->>Script: Trigger
    Script->>PyPI: Async query 1,045 packages
    Script->>Pulp: Async query published versions
    PyPI-->>Script: Available versions
    Pulp-->>Script: Already-published versions
    Script->>Script: Filter pre-releases, yanked, ignored
    Script->>Repo: Create PR per new version
    Repo->>Repo: Auto-merge (rebase)
    Repo->>Repo: Tekton pipeline triggered") }}

{{ callout("<strong>Async queries</strong> - all 1,045 packages checked concurrently.<br><strong>Smart filtering</strong> - pre-releases, yanked releases, and <code>ignored_versions</code> all excluded.<br><strong>Labels:</strong> PRs tagged \"automated build\" for tracking.") }}
