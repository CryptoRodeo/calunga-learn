# Support Matrix & Roadmap

<div class="grid cards" markdown>

-   __Python Versions__{ style="color:#009596;" }

    ---

    | Version | Status |
    |---------|--------|
    | Python 2.x | <span style="color:#f44;">Not supported</span> |
    | Python 3.9 – 3.10 | <span style="color:#f44;">Not supported</span> |
    | **Python 3.12** | <span style="color:#3e8635;">Fully supported</span> |
    | Python 3.11, 3.13, 3.14 | <span style="color:#f0ab00;">Planned</span> |

-   __Architectures__{ style="color:#009596;" }

    ---

    | Arch | Status |
    |------|--------|
    | **x86_64** | <span style="color:#3e8635;">Fully supported</span> |
    | aarch64 | <span style="color:#f0ab00;">Planned</span> |

    ### Manylinux Target

    Primary: `manylinux_2_28` (glibc 2.28+, RHEL 8+).
    Some wheels also carry `manylinux_2_27` compatibility.

</div>

### Alternative Python Runtimes

The builder image includes multiple Python runtimes beyond CPython, all SHA256-pinned:

| Runtime | Versions | Architectures |
|---------|----------|---------------|
| **CPython** | 3.12.12 (from source) | x86_64, aarch64 |
| **PyPy** | 3.8 – 3.11 | x86_64, aarch64, i686 |
| **GraalPy** | 3.11 (24.2.2), 3.12 (25.0.1) | x86_64, aarch64 |

!!! note ""

    All interpreter downloads are pinned by SHA256 hash in `python_versions.json` for reproducibility.
