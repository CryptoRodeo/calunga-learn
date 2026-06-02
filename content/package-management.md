---
id: package-management
title: "Index: Package Management"
---

### 1,045 Onboarded Packages

Each package has a JSON file in `onboarded_packages/`:

```json
{
  "version": "2.4.6",
  "ignored_versions": ["0.9.6", "0.9.8", "2.4.3"]
}
```

- `version` — current target version to build
- `ignored_versions` — unsupported, vulnerable, or skipped releases

{{ callout("One JSON file = one Python package. Simple contract between version detection and build pipeline.", style="teal") }}

### Package Lifecycle

{{ flow_steps_start() }}
{{ flow_step(1, "<code>check-for-updates.py</code> queries PyPI + Pulp (every 12h)") }}
{{ flow_step(2, "Filters pre-releases and yanked versions") }}
{{ flow_step(3, "Creates PR per new version (updates JSON)") }}
{{ flow_step(4, "PR auto-merged (rebase strategy)") }}
{{ flow_step(5, "Merge triggers Tekton PipelineRun") }}
{{ flow_step(6, "<code>identify-packages</code> detects changed JSONs") }}
{{ flow_step(7, "Invokes <code>build-python-wheels</code> task") }}
{{ flow_step(8, "Wheels scanned &rarr; released &rarr; published") }}
{{ flow_steps_end() }}
