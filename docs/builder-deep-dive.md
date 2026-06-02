# Builder Image: Source-Built Libraries

<div class="grid" markdown>

<div markdown>

| Library | Version | Why |
|---------|---------|-----|
| OpenSSL | 3.5.4 | TLS, cryptography wheels |
| curl | 8.17.0 | HTTP client for downloads |
| git | 2.51.2 | Source fetching |
| SQLite | 3.51.0 | Python stdlib module |
| OpenBLAS | latest | NumPy/SciPy linear algebra |
| libjpeg-turbo | latest | Pillow image processing |
| libxml2 / libxslt | latest | lxml XML parsing |
| libyaml | latest | PyYAML C extension |
| zlib / bzip2 / zstd | latest | Compression |
| libffi | latest | ctypes / cffi |
| mpdecimal | latest | Python decimal module |
| libomp | latest | OpenMP parallelism |
| libpng / libtiff | latest | Image format support |

</div>

<div markdown>

### Build Details

- **Base:** UBI8 (RHEL 8 userspace)
- **Python:** CPython 3.12.12 from source
- **Alt runtime:** PyPy 3.11
- **Alt runtime:** GraalPy 3.11 / 3.12
- **C/C++:** gcc-toolset-14
- **C/C++ (static):** clang 21.1.5
- **Rust:** 1.95.0
- **Deps:** pip-compile --require-hashes

### Key Tools

- **Fromager** - orchestrates full dep graph builds
- **auditwheel** - bundles .so, sets manylinux tag
- **pip-compile** - hash-pinned requirements

</div>

</div>
