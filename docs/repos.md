# Two Repos, One System

<div class="grid cards" markdown>

-   __calunga-project-plumbing__{ style="color:#009596;" }

    ---

    <p style="color:#009596; font-size:0.9rem;">Build Infrastructure</p>

    - Container images (builder, utils)
    - Tekton tasks & pipelines
    - Build scripts (Fromager, auditwheel)
    - SBOM patching & artifact collection

    <div class="dir-tree">
    builder/<br>├── Containerfile &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Multi-stage builder image<br>├── build_scripts/ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# 43 build &amp; install scripts<br>├── scripts/ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# build-wheels entry point<br>└── tests/<br>tasks/ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Tekton bundles<br>pipelines/ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# integration tests
    </div>

-   __calunga-project-index__{ style="color:#009596;" }

    ---

    <p style="color:#009596; font-size:0.9rem;">Package Registry</p>

    - 1,045 onboarded package JSONs
    - Version detection (12h cron)
    - Auto-PR creation & merge
    - Konflux release pipeline

    <div class="dir-tree">
    onboarded_packages/<br>├── numpy.json<br>├── requests.json<br>└── ... (1,045 files)<br>hack/ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# check-for-updates.py<br>.tekton/ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# build-pipeline.yaml
    </div>

</div>

!!! note ""

    **plumbing** builds the tools → **index** uses them to build wheels → wheels published to **packages.redhat.com**
