---
id: observability
title: Observability
---

{{ two_col_start() }}
{{ card("Log Forwarding") }}

A separate GitHub Actions workflow (`forward_logs.yml`) triggers after every version-check run:

{{ flow_steps_start() }}
{{ flow_step(1, "<code>get_new_package_versions</code> workflow completes", color="teal") }}
{{ flow_step(2, "Log forwarder downloads full run log via <code>gh run view --log</code>", color="teal") }}
{{ flow_step(3, "Logs POSTed to Splunk endpoint (token-authenticated)", color="teal") }}
{{ flow_steps_end() }}

{{ card_end() }}
{{ card("PR Tracking") }}

- Automated version PRs labeled **"automated build"**
- Konflux nudge PRs labeled **"konflux-nudge"**
- Branch naming: `update-<package>==<version>`
- All PRs auto-merged with rebase strategy

### Build Artifacts

- PR builds expire after **5 days**
- Push builds permanent (tagged by git revision)
- All images referenced by **SHA256 digest**

{{ card_end() }}
{{ two_col_end() }}
