---
id: integration-testing
title: Integration Testing
---

{{ two_col_start() }}
<div>

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
<div>

### Per-Wheel Test Steps

{{ flow_steps_start() }}
{{ flow_step(1, "Install wheel with pip/uv") }}
{{ flow_step(2, "Verify import succeeds") }}
{{ flow_step(3, "Check manylinux tag correct") }}
{{ flow_step(4, "Verify SBOM present (redhat.spdx.json)") }}
{{ flow_step(5, "Validate PURL qualifiers") }}
{{ flow_steps_end() }}

{{ callout("Pipeline: <code>install-and-import-wheels.yaml</code><br>Spans both repos — plumbing defines it, index triggers it.") }}

</div>
{{ two_col_end() }}
