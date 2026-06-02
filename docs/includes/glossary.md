*[Fromager]: Python wheel build orchestrator. Resolves full dependency graph from source distributions, builds each package in order, and embeds CycloneDX SBOMs.
*[auditwheel]: Post-build compliance tool. Inspects Linux wheels for shared library deps, bundles required .so files, relabels with correct manylinux platform tag.
*[Tekton]: Kubernetes-native CI/CD framework. Pipelines defined as YAML CRDs.
*[Konflux]: Red Hat's enterprise CI/CD platform built on Tekton.
*[CycloneDX]: SBOM standard. Fromager generates CycloneDX SBOMs embedded as redhat.spdx.json.
*[cosign]: Sigstore tool for signing and verifying container images and artifacts.
*[UBI8]: Universal Base Image. Red Hat's freely redistributable container base (RHEL 8 userspace).
*[Buildah]: Daemonless container image builder. Builds OCI/Docker images from Containerfiles.
*[Nudge]: Konflux auto-update mechanism for pinned SHA256 references.
*[manylinux]: PEP-defined Linux wheel compatibility standard specifying max glibc version.
*[gcc-toolset-14]: Red Hat's SCL-packaged GCC 14 for UBI8/RHEL 8.
*[pip-compile]: Dependency resolver from pip-tools. Generates pinned requirements.txt with SHA256 hashes.
*[Enterprise Contract Policy]: Konflux policy framework validating builds meet Red Hat compliance.
*[OCI Trusted Artifacts]: Konflux pattern for passing data between Tekton tasks via OCI artifacts.
