# Getting Started

To install wheels from Red Hat Trusted Libraries, you need a **service account** from the
[terms-based registry](https://access.redhat.com/terms-based-registry/accounts)
and **Python 3.12** installed on your system.

<div class="grid cards" markdown>

-   __pip Configuration__{ style="color:#009596;" }

    ---

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

-   __uv Configuration__{ style="color:#009596;" }

    ---

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

</div>

### Viewing SBOMs

Every wheel contains an SBOM at `<package>.dist-info/sboms/redhat.spdx.json`:

```
pip download numpy==2.3.3
unzip numpy-2.3.3-0-cp312-cp312-manylinux_2_28_x86_64.whl -d extracted
cat extracted/numpy-2.3.3.dist-info/sboms/redhat.spdx.json
```

!!! info ""

    **Provenance verification:** Attestations can be verified using cosign. See [verification scripts](https://github.com/redhat-tssc-tmm/trusted-libraries/tree/main/blog/scripts) for examples.
