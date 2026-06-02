# Technology Glossary

<div class="glossary-grid">
<div class="glossary-card" id="gl-fromager"><strong>Fromager</strong> Python wheel build orchestrator. Resolves full dependency graph from source distributions, builds each package in order, embeds CycloneDX SBOMs. Ensures wheels built from source - not pre-built from PyPI.</div>
<div class="glossary-card" id="gl-auditwheel"><strong>auditwheel</strong> Post-build compliance tool. Inspects Linux wheels for shared library deps, bundles required .so files, relabels with correct manylinux platform tag (e.g., manylinux_2_28).</div>
<div class="glossary-card" id="gl-tekton"><strong>Tekton</strong> Kubernetes-native CI/CD. Pipelines defined as YAML CRDs (Tasks, Pipelines, PipelineRuns). Each step runs in its own container. Used here via Konflux.</div>
<div class="glossary-card" id="gl-konflux"><strong>Konflux</strong> Red Hat's enterprise CI/CD on Tekton. Adds Enterprise Contract Policy, release management, nudge-based auto-updates, and OCI Trusted Artifacts.</div>
<div class="glossary-card" id="gl-buildah"><strong>Buildah</strong> Daemonless container builder. Builds OCI/Docker images from Containerfiles without Docker daemon. Used by Tekton tasks for builder/utils images.</div>
<div class="glossary-card" id="gl-twine"><strong>Twine</strong> Python package upload tool. Publishes wheels to PyPI-compatible registries (here: Red Hat's Pulp at packages.redhat.com).</div>
<div class="glossary-card" id="gl-ubi"><strong>UBI</strong> Universal Base Image. Red Hat's freely redistributable minimal container base. UBI8 = RHEL 8 userspace (builder), UBI10 = RHEL 10 (utils/index).</div>
<div class="glossary-card" id="gl-pip-compile"><strong>pip-compile</strong> Dependency resolver (pip-tools). Generates pinned requirements.txt with SHA256 hashes from loose requirements.in. Ensures reproducible installs.</div>
<div class="glossary-card" id="gl-oci-ta"><strong>OCI Trusted Artifacts</strong> Konflux pattern: pass data between Tekton tasks via OCI artifacts in a registry, not shared PVCs. Immutable and auditable.</div>
<div class="glossary-card" id="gl-cosign"><strong>cosign</strong> Sigstore tool for signing/verifying container images and artifacts. Used for attestation and provenance in the release pipeline.</div>
<div class="glossary-card" id="gl-pulp"><strong>Pulp</strong> Red Hat's repository management platform. Hosts the RHTL Python package index. Version-detection cron checks Pulp for already-published versions.</div>
<div class="glossary-card" id="gl-ecp"><strong>Enterprise Contract Policy (ECP)</strong> Konflux policy framework. Validates builds meet Red Hat compliance (provenance, signatures, SBOM) before allowing releases.</div>
<div class="glossary-card" id="gl-cyclonedx"><strong>CycloneDX / SPDX</strong> SBOM standards. Fromager generates CycloneDX SBOMs embedded as redhat.spdx.json, listing components and provenance.</div>
<div class="glossary-card" id="gl-manylinux"><strong>manylinux</strong> PEP-defined Linux wheel compatibility standard. Specifies max glibc version and allowed shared libs. manylinux_2_28 = glibc 2.28+ (RHEL 8+).</div>
<div class="glossary-card" id="gl-gcc"><strong>gcc-toolset-14</strong> Red Hat's SCL-packaged GCC 14 for UBI8/RHEL 8. Modern C/C++ compilation without replacing system GCC.</div>
<div class="glossary-card" id="gl-nudge"><strong>Nudge</strong> Konflux auto-update mechanism. When plumbing publishes new image/task digest, nudge creates PRs in downstream repos to update pinned SHA256 refs.</div>
<div class="glossary-card" id="gl-graalpy"><strong>GraalPy</strong> Oracle's Python implementation on GraalVM. Supports 3.11 and 3.12. Included in builder for alternative runtime wheel compatibility testing. SHA256-pinned downloads.</div>
<div class="glossary-card" id="gl-pep740"><strong>PEP 740</strong> Python standard for digital attestations on packages. Defines how provenance metadata is attached to wheels for upload to PyPI-compatible registries. Calunga converts DSSE envelopes to PEP 740 format.</div>
</div>
