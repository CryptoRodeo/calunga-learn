---
id: getting-started
title: Getting Started
---

To install wheels from Red Hat Trusted Libraries, you need a **service account** from the
<a href="https://access.redhat.com/terms-based-registry/accounts" style="color:var(--rh-teal);">terms-based registry</a>
and **Python 3.12** installed on your system.

{{ two_col_start() }}
{{ card("pip Configuration") }}

```
# pip.conf (venv/, ~/.config/pip/, or /etc/pip.conf)
[global]
index-url = https://<username>:<password>@packages.redhat.com/trusted-libraries/python/
```

```
# Install packages
python3.12 -m venv venv && source venv/bin/activate
pip install numpy
pip install --only-binary=:all: -r requirements.txt
```

{{ card_end() }}
{{ card("uv Configuration") }}

```
# pyproject.toml
[[tool.uv.index]]
name = "trusted-libraries"
url = "https://packages.redhat.com/trusted-libraries/python"
default = true
```

```
# Export credentials
export UV_INDEX_INTERNAL_PROXY_USERNAME=<username>
export UV_INDEX_INTERNAL_PROXY_PASSWORD=<password>
```

{{ card_end() }}
{{ two_col_end() }}

### Viewing SBOMs

Every wheel contains an SBOM at `<package>.dist-info/sboms/redhat.spdx.json`:

```
pip download numpy==2.3.3
unzip numpy-2.3.3-0-cp312-cp312-manylinux_2_28_x86_64.whl -d extracted
cat extracted/numpy-2.3.3.dist-info/sboms/redhat.spdx.json
```

{{ callout("<strong>Provenance verification:</strong> Attestations can be verified using cosign. See <a href='https://github.com/redhat-tssc-tmm/trusted-libraries/tree/main/blog/scripts' style='color:var(--rh-teal);'>verification scripts</a> for examples.", style="teal") }}
