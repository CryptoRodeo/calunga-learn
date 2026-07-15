---
id: repos
title: Seven Repos, One System
---

{{ two_col_start() }}
{{ card("calunga-project-plumbing") }}

<p style="color:var(--rh-teal); font-size:0.9rem;">Build Infrastructure</p>

- Container images (builder, utils)
- {{ glossary("Tekton", "Kubernetes-native CI/CD framework. Pipelines defined as YAML CRDs (Tasks, Pipelines, PipelineRuns). Each step runs in its own container. Used here via Konflux.") }} tasks & pipelines
- Build scripts ({{ glossary("Fromager", "Python wheel build orchestrator. Resolves full dependency graph from source distributions, builds each package in order, and embeds CycloneDX SBOMs. Ensures wheels are built from source - not downloaded pre-built from PyPI.") }}, {{ glossary("auditwheel", "Post-build compliance tool. Inspects Linux wheels for shared library dependencies, bundles required .so files into the wheel, and relabels it with the correct manylinux platform tag.") }})
- SBOM patching & artifact collection

{{ dir_tree("builder/<br>├── Containerfile &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Multi-stage builder image<br>├── build_scripts/ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# 37 build &amp; install scripts<br>├── scripts/ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# build-wheels entry point<br>└── tests/<br>tasks/ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Tekton bundles<br>pipelines/ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# integration tests") }}

{{ card_end() }}
{{ card("calunga-project-index") }}

<p style="color:var(--rh-teal); font-size:0.9rem;">Package Registry</p>

- 1,547 onboarded package JSONs
- Version detection (12h cron)
- Auto-PR creation & merge
- {{ glossary("Konflux", "Red Hat's enterprise CI/CD platform built on Tekton. Adds Enterprise Contract Policy enforcement, release management, nudge-based auto-updates, and OCI Trusted Artifacts for secure data passing between tasks.") }} release pipeline

{{ dir_tree("onboarded_packages/<br>├── numpy.json<br>├── requests.json<br>└── ... (1,547 files)<br>hack/ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# check-for-updates.py<br>.tekton/ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# build-pipeline.yaml") }}

{{ card_end() }}
{{ two_col_end() }}

{{ callout("<strong>plumbing</strong> builds the tools &rarr; <strong>index</strong> uses them to build wheels &rarr; wheels published to <strong>packages.redhat.com</strong>") }}

### Companion Repositories

{{ two_col_start() }}
{{ card("npm-registry") }}

<p style="color:var(--rh-teal); font-size:0.9rem;">npm Package Onboarding</p>

- npm package definitions (`packages/`)
- Lint &amp; identification scripts (`hack/`)
- Tekton build pipeline (`.tekton/`)

{{ card_end() }}
{{ card("check-source-origin") }}

<p style="color:var(--rh-teal); font-size:0.9rem;">Source Verification</p>

- Python CLI: verify published sdists match VCS source
- Commands: resolve, download, diff, verify

{{ card_end() }}
{{ two_col_end() }}

{{ two_col_start() }}
{{ card("dfd (Dumpster Fire Diving)") }}

<p style="color:var(--rh-teal); font-size:0.9rem;">CI Failure Analysis</p>

- AI-powered failure analysis (FastAPI + Claude)
- React dashboard
- KubeArchive collector

{{ card_end() }}
{{ card("bounty-board") }}

<p style="color:var(--rh-teal); font-size:0.9rem;">Package Prioritization</p>

- Package prioritization tracker
- Python scripts + GitHub Actions
- Static HTML dashboard

{{ card_end() }}
{{ two_col_end() }}

{{ two_col_start() }}
{{ card("wheel-patcher") }}

<p style="color:var(--rh-teal); font-size:0.9rem;">Wheel Post-Processing</p>

- Patch wheel files (add SBOM, license files)
- Zero runtime dependencies

{{ card_end() }}
<div></div>
{{ two_col_end() }}
