# Quick Reference

<div class="grid" markdown>

<div markdown>

### Key Paths (Plumbing)

| Path | Purpose |
|------|---------|
| `builder/Containerfile` | Main builder image (2000+ lines) |
| `builder/scripts/build-wheels` | Wheel build entry point |
| `builder/build_scripts/` | 17 library build scripts |
| `builder/requirements.txt` | Hash-pinned Fromager deps |
| `tasks/build-python-wheels-oci-ta.yaml` | Tekton task definition |
| `pipelines/wheel-integration-test.yaml` | Cross-OS test pipeline |
| `utils/scripts/pulp-upload` | Pulp registry upload with attestation |
| `utils/scripts/generate-and-sign-attestations` | cosign attestation + PEP 740 conversion |
| `.tekton/` | PipelineRun definitions |

### Key Paths (Index)

| Path | Purpose |
|------|---------|
| `onboarded_packages/*.json` | 1,045 package definitions |
| `hack/check-for-updates.py` | Version detection script |
| `hack/identify-packages` | Changed-package detector |
| `hack/onboard_package.py` | New package onboarding script |
| `.tekton/build-pipeline.yaml` | Main build pipeline |
| `konflux/ecp.yaml` | Enterprise Contract Policy |

</div>

<div markdown>

### User Configuration

```
# pip.conf
[global]
extra-index-url =
    https://packages.redhat.com/trusted-libraries/python/simple/
```

```
# pyproject.toml (uv)
[[tool.uv.index]]
url = "https://packages.redhat.com/trusted-libraries/python/simple/"
name = "rhtl"
```

### Key Numbers

| Metric | Value |
|--------|-------|
| Packages | **1,045+** |
| Source-built libs | **17** |
| Security scans | **6 types** |
| Test OS targets | **6** |
| Pipeline tasks | **17** |
| Version check interval | **12 hours** |
| Release grace period | **7 days** |

</div>

</div>
