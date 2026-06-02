---
id: integration-testing
title: Integration Testing
---

{{ two_col_start() }}
<div markdown="1">

### Cross-OS Verification

Built wheels tested across **6 OS images**:

{{ flow_steps_start() }}
{{ flow_step(1, "UBI8 (RHEL 8)", color="teal") }}
{{ flow_step(2, "UBI9 (RHEL 9)", color="teal") }}
{{ flow_step(3, "UBI10 (RHEL 10)", color="teal") }}
{{ flow_step(4, "Fedora 43", color="teal") }}
{{ flow_step(5, "Ubuntu 24.04", color="teal") }}
{{ flow_step(6, "Hummingbird", color="teal") }}
{{ flow_steps_end() }}

</div>
<div markdown="1">

### Per-Wheel Test Steps

{{ flow_steps_start() }}
{{ flow_step(1, "Classify wheel (skip empty/data-only)") }}
{{ flow_step(2, "Install wheel with pip/uv in fresh venv") }}
{{ flow_step(3, "Verify import succeeds") }}
{{ flow_steps_end() }}

{{ callout("Pipeline: <code>install-and-import-wheels.yaml</code><br>Spans both repos - plumbing defines it, index triggers it.") }}

</div>
{{ two_col_end() }}
