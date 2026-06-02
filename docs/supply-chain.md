# Supply Chain Security

<div class="security-grid">
<div class="security-item"><span class="icon">&#x1f512;</span><div><strong>Hash Pinning</strong><br>All Python deps use --require-hashes. Container/task refs pinned by SHA256.</div></div>
<div class="security-item"><span class="icon">&#x1f3d7;&#xfe0f;</span><div><strong>Source Builds</strong><br>17 C/C++ libs compiled from source with verified checksums. No pre-built binaries.</div></div>
<div class="security-item"><span class="icon">&#x1f4cb;</span><div><strong>SBOM Embedding</strong><br>Every wheel contains redhat.spdx.json with supplier info and PURLs.</div></div>
<div class="security-item"><span class="icon">&#x1f50d;</span><div><strong>Security Scanning</strong><br>6 scans per build: Clair, Snyk, ClamAV, Coverity, ShellCheck, Unicode.</div></div>
<div class="security-item"><span class="icon">&#x1f4dc;</span><div><strong>Enterprise Contract Policy</strong><br>Red Hat compliance enforcement on every release.</div></div>
<div class="security-item"><span class="icon">&#x270d;&#xfe0f;</span><div><strong>Attestation</strong><br>Provenance and signing via cosign (Sigstore).</div></div>
<div class="security-item"><span class="icon">&#x1f3e0;</span><div><strong>Hermetic Builds</strong><br>Optional fully isolated mode - zero network access during build.</div></div>
<div class="security-item"><span class="icon">&#x1f4e6;</span><div><strong>OCI Trusted Artifacts</strong><br>Data passes between tasks via OCI artifacts, not shared volumes.</div></div>
</div>
