---
id: builder-tests
title: "Builder Image: Self-Tests"
---

The builder image runs a comprehensive test suite (`builder/tests/run_tests.sh`) to validate every component before any wheel build occurs.

{{ security_grid_start() }}
{{ security_item("&#x1f40d;", "Interpreter Count", "Verifies expected number of Python installations (CPython, PyPy, GraalPy) are present and functional.") }}
{{ security_item("&#x1f512;", "SSL Validation", "Every interpreter tested for correct OpenSSL configuration and cert verification.") }}
{{ security_item("&#x1f4e6;", "Module Check", "CPython optional modules (sqlite3, ssl, ctypes, decimal, etc.) verified loadable.") }}
{{ security_item("&#x2699;&#xfe0f;", "Wheel Build + Repair", "C extension project (<code>forty-two</code>) built, repaired with auditwheel, installed and executed per interpreter.") }}
{{ security_item("&#x1f50d;", "Library Discovery", "Source-built libs verified via <code>pkg-config</code> and <code>ldconfig</code> (libjpeg, libyaml, libxml2, etc.).") }}
{{ security_item("&#x1f3d7;&#xfe0f;", "Compile Tests", "Autotools and CMake projects compiled against installed headers and libraries (SQLite, C++).") }}
{{ security_item("&#x1f6e0;&#xfe0f;", "Tool Presence", "auditwheel, autoconf, automake, libtool, patchelf, git, git-lfs, cmake, swig, nox all verified.") }}
{{ security_item("&#x1f4bb;", "uv Integration", "Wheels installed via both pip and uv to verify compatibility with modern tooling.") }}
{{ security_grid_end() }}

{{ callout("Tests run on every PR via GitHub Actions. Path filtering skips the full build when only non-builder files change.", style="teal") }}
