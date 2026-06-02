# Builder Image: Self-Tests

The builder image runs a comprehensive test suite (`builder/tests/run_tests.sh`) to validate every component before any wheel build occurs.

<div class="security-grid">
<div class="security-item"><span class="icon">&#x1f40d;</span><div><strong>Interpreter Count</strong><br>Verifies expected number of Python installations (CPython, PyPy, GraalPy) are present and functional.</div></div>
<div class="security-item"><span class="icon">&#x1f512;</span><div><strong>SSL Validation</strong><br>Every interpreter tested for correct OpenSSL configuration and cert verification.</div></div>
<div class="security-item"><span class="icon">&#x1f4e6;</span><div><strong>Module Check</strong><br>CPython optional modules (sqlite3, ssl, ctypes, decimal, etc.) verified loadable.</div></div>
<div class="security-item"><span class="icon">&#x2699;&#xfe0f;</span><div><strong>Wheel Build + Repair</strong><br>C extension project (<code>forty-two</code>) built, repaired with auditwheel, installed and executed per interpreter.</div></div>
<div class="security-item"><span class="icon">&#x1f50d;</span><div><strong>Library Discovery</strong><br>Source-built libs verified via <code>pkg-config</code> and <code>ldconfig</code> (libjpeg, libyaml, libxml2, etc.).</div></div>
<div class="security-item"><span class="icon">&#x1f3d7;&#xfe0f;</span><div><strong>Compile Tests</strong><br>Autotools and CMake projects compiled against installed headers and libraries (SQLite, C++).</div></div>
<div class="security-item"><span class="icon">&#x1f6e0;&#xfe0f;</span><div><strong>Tool Presence</strong><br>auditwheel, autoconf, automake, libtool, patchelf, git, git-lfs, cmake, swig, nox all verified.</div></div>
<div class="security-item"><span class="icon">&#x1f4bb;</span><div><strong>uv Integration</strong><br>Wheels installed via both pip and uv to verify compatibility with modern tooling.</div></div>
</div>

!!! info ""

    Tests run on every PR via GitHub Actions. Path filtering skips the full build when only non-builder files change.
